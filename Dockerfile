# 使用 AWS 提供的 Lambda Python 3.11 基礎鏡像
FROM public.ecr.aws/lambda/python:3.11

# 設定工作目錄
WORKDIR /var/task

# 複製所有檔案到容器內
COPY . .

# 如果有安裝套件的需求，確保有 requirements.txt
COPY requirements.txt .

# 安裝必要的套件
RUN pip install --no-cache-dir -r requirements.txt

# 安裝一些常用的系統套件（按需要增減）
RUN yum update -y && \
    yum install -y \
    gcc \
    make \
    curl \
    unzip \
    && yum clean all

# 設定環境變數（按需要修改）
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV TZ=Asia/Taipei

# 設定時區
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 設定權限
RUN chmod 755 /var/task

# 設定 Lambda 入口函數（Lambda 會呼叫 main.lambda_handler）
CMD ["main.lambda_handler"]