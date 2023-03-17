FROM my_own_repo/ubuntu_with_all_i_need_to_build:latest as base
WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json

FROM base as test
RUN npm ci
COPY . .
CMD [ "npm", "run", "test" ]

FROM base as builder
RUN npm install && \
	npm run build

FROM my_own_repo/ubuntu_with_all_i_need_to_run:latest as runner
RUN groupadd -r appuser -g 433 && \
    useradd -u 431 -r -g swuser -s /sbin/nologin -c "Docker image user" appuser
USER appuser

WORKDIR /app
COPY --from=builder /app/what_ever_is_required ./
ENTRYPOINT ["npm", "run"]
CMD ["develop"]
