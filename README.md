# Vue.js-Django 프로그래밍(실전편)

### \_get_next_or_previous_by_FIELD

1. previous : field를 기준으로 이전 객체를 리턴함
2. next : field를 기준으로 다음 객체를 리턴함

```python
# django.db.models.base.py
 def _get_next_or_previous_by_FIELD(self, field, is_next, **kwargs):
        if not self.pk:
            raise ValueError("get_next/get_previous cannot be used on unsaved objects.")
        op = "gt" if is_next else "lt"
        order = "" if is_next else "-"
        param = getattr(self, field.attname)
        q = Q((field.name, param), (f"pk__{op}", self.pk), _connector=Q.AND)
        q = Q(q, (f"{field.name}__{op}", param), _connector=Q.OR)
        qs = (
            self.__class__._default_manager.using(self._state.db)
            .filter(**kwargs)
            .filter(q)
            .order_by("%s%s" % (order, field.name), "%spk" % order)
        )
        try:
            return qs[0]
        except IndexError:
            raise self.DoesNotExist(
                "%s matching query does not exist." % self.__class__._meta.object_name
```

### Blog URL 설계

| URL Pattern      | View Name             | Template Name    |
| ---------------- | --------------------- | ---------------- |
| /admin           | (Defualt Django)      |                  |
| /                | HomeView(TemplateView | home.html        |
|                  |                       |                  |
| /blog/post/list/ | PostLV(ListView)      | post_list.html   |
| /blog/post/99/   | PostDV(DetailView)    | post_detail.html |

### User(더 공부해야 함)

프로젝트 초기에 잘 설정해야 함
| URL Pattern | (1)Proxy | (2)Profile|(3)AbstractUser|(4)AbstractBaseUser|
| ---------------- | :---: | :---: |:---:|:---:|
| 컬럼 변경이 없으면? | o | |||
| 기본 User 테이블을 사용하면? | | o |||
| username 컬럼을 사용하면?| | |o||
| username 컬럼을 사용안하면? | | | | o|

### Deployment checklist(더 공부해야 함)

[공식문서 링크](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)
settings.py 분리하기

1. base.py : 공통 항목
2. develop.py : 개발모드 에 필요한 항목
3. product.py : 운영모드에서 필요한 항목

### Vue

main.js -> App.vue -> components/HelloWorld.vue 순으로 수행됨

```
npm run serve
vue add vuetify
```

vuetify 는 vue.js 3 version 에서 지원하지 않음
vue.js version 2.\*로 프로젝트를 설치해야 함

### component 등록

```javascript
import HelloWorld from "./components/HelloWorld.vue";
export default {
  components: { HelloWorld },
  data: () => ({})

```

### Django 연동을 위한 vue.config.js 수정

Django는 /static/ URL을 가지고 찾기 때문에 vue.config.js 파일 수정 후

- FrontEnd의 css, img, js 폴더를 static 폴더 밑으로 옮긴 후 다시 Build
- frontend dist의 static 하위 폴더를 django static 폴더로 이동
- frontend dist의 index.html을 django templates 폴더로 이동

Django MVT 패턴으로 설명하면

- Model, View 생성
- Templates => vue 프로젝트 webpack 을 사용해 만듬

[공식문서](https://cli.vuejs.org/config/#publicpath)

```javascript
const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],

  outputDir: "dist",
  publicPath: "/",
  assetsDir: "static",
});
```

- 여러개의 page를 만들기 위한 vue.config.js 수정
  - [GITHUB](https://github.com/jantimon/html-webpack-plugin)
  - [공식문서](https://cli.vuejs.org/config/#pages)

* SPA vs MPA
  현재 프로젝트에서는 MPA로 구현

```javascript
  pages: {
    home: {
      template: "public/index.html",
      entry: "src/pages/main_home.js",
      filename: "home.html",
      title: "VueDjangoPhoto/home.html",
      minify: false,
    },
  }
```

- root url 변경

* webpack 개발 서버가 root url에 대해 defualt로 index.html을 찾기 떄문에

```javascript
// vue.config.js 추가
devServer: {
    static: {
      directory: path.join(__dirname, "dist"),
      staticOptions: {
        index: "home.html",
      },
    },
  },

```

### MPA 정리

1. Multiple page 구현을 위해 vue.config.js 파일 수정
2. 생성할 페이지를 정의 후 등록
3. vue파일과 js파일 생성 및 component 등록

### FileManagerPlugin

빌드 전후에 파일과 디렉토리를 복사, 이동, 삭제할 수 있음

[공식문서](https://www.npmjs.com/package/filemanager-webpack-plugin)

- 설치

```
npm install filemanager-webpack-plugin --save-dev
```

### Vuetify Spacing

Components 스타일 정의
[공식문서](https://vuetifyjs.com/en/styles/spacing/)

### API

### Blog URL 설계

| URL Pattern     | View Name                   | Template Name |
| --------------- | --------------------------- | ------------- |
| /api/post/list/ | ApiPostLV(BaseListView)     |               |
| /api/post/99/   | ApiPostDV(BaseDetailView)   |               |
| /api/tag/cloud  | ApiTagCloudLV(BaseListView) |               |
