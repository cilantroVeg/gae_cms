# source2swagger -i /Users/arturo/interpegasus/gae_cms/projects/cms/static/template/API/specs/ -e "rb" -c "##~" -o /Users/arturo/interpegasus/gae_cms/projects/cms/static/template/API/api-docs
# find ./ -name "*.json" -exec sh -c 'mv $0 `basename "$0" .json`' '{}' \;


##~ a = source2swagger.namespace("interpegasus_cms")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/languages", :description => "Get CMS Available Languages", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Languages", :responseClass => "LanguageArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"

##~ a.models["Language"] = {:id => "Language", :properties => {:language => {:type => "string"}, :code => {:type => "string"}}}
##~ a.models["LanguageArray"] = {:id => "LeagueArray", :properties => {:languages => {:type => "Array", :items =>{:$ref => "Language"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def languages
  return
end


##~ a = source2swagger.namespace("interpegasus_cms")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/categories", :description => "Get CMS Categories by language", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Categories", :responseClass => "CategoryArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "category_slug", :description => "get subcategories for category slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Category"] = {:id => "Category", :properties => {:name => {:type => "string"}, :parent => {:type => "string"}}}
##~ a.models["CategoryArray"] = {:id => "CategoryArray", :properties => {:categories => {:type => "Array", :items =>{:$ref => "Category"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def categories
  return
end


##~ a = source2swagger.namespace("interpegasus_cms")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/pages", :description => "Get pages by slug or by category", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Page", :responseClass => "PageArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "page_slug", :description => "page slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"
##~ o.parameters.add :name => "category_slug", :description => "category slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Page"] = {:id => "Page", :properties => {:title => {:type => "string"}, :content => {:type => "string"}}}
##~ a.models["PageArray"] = {:id => "PageArray", :properties => {:pages => {:type => "Array", :items =>{:$ref => "Page"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def pages
  return
end


##~ a = source2swagger.namespace("interpegasus_cms")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/images", :description => "Get images by slug or by category", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Image", :responseClass => "ImageArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "page_slug", :description => "page slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Image"] = {:id => "Image", :properties => {:title => {:type => "string"}, :url => {:type => "string"}}}
##~ a.models["ImageArray"] = {:id => "ImageArray", :properties => {:images => {:type => "Array", :items =>{:$ref => "Image"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def images
  return
end

##~ a = source2swagger.namespace("interpegasus_cms")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/feed_pages", :description => "Get feed pages", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Feed Pages", :responseClass => "PageArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "page_slug", :description => "page slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Page"] = {:id => "Page", :properties => {:title => {:type => "string"}, :content => {:type => "string"}}}
##~ a.models["PageArray"] = {:id => "PageArray", :properties => {:pages => {:type => "Array", :items =>{:$ref => "Page"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def pages
  return
end


##~ a = source2swagger.namespace("bible")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/books", :description => "Get book names", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Bible Books", :responseClass => "BookArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "testament", :description => "Possible Values: old testament, new testament", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"

##~ a.models["Book"] = {:id => "Book", :properties => {:title => {:type => "string"}}}
##~ a.models["BookArray"] = {:id => "BookArray", :properties => {:books => {:type => "Array", :items =>{:$ref => "Book"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def books
  return
end

##~ a = source2swagger.namespace("bible")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/chapters", :description => "Get chapters by book", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Bible Chapters by book", :responseClass => "ChapterArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "book_code", :description => "book code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "chapter_number", :description => "Chapter Number", :dataType => "int", :allowMultiple => false, :required => false, :paramType => "query"
##~ o.parameters.add :name => "versicle_number", :description => "Versicle Number", :dataType => "int", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Versicle"] = {:id => "Versicle", :properties => {:number => {:type => "int"}, :content => {:type => "string"}}}
##~ a.models["Chapter"] = {:id => "Chapter", :properties => {:versicles => {:type => "Array",:items =>{:$ref => "Versicle"} }}}
##~ a.models["ChapterArray"] = {:id => "ChapterArray", :properties => {:chapters => {:type => "Array", :items =>{:$ref => "Chapter"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def chapters
  return
end

##~ a = source2swagger.namespace("nrwl")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/categories", :description => "Get NRWL Categories by language", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Categories", :responseClass => "CategoryArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "category_slug", :description => "get subcategories for category slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Category"] = {:id => "Category", :properties => {:name => {:type => "string"}, :parent => {:type => "string"}}}
##~ a.models["CategoryArray"] = {:id => "CategoryArray", :properties => {:categories => {:type => "Array", :items =>{:$ref => "Category"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def categories
  return
end


##~ a = source2swagger.namespace("nrwl")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/pages", :description => "Get NRWL pages by slug or by category", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Page", :responseClass => "PageArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "page_slug", :description => "page slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"
##~ o.parameters.add :name => "category_slug", :description => "get pages for category", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Page"] = {:id => "Page", :properties => {:title => {:type => "string"}, :content => {:type => "string"}}}
##~ a.models["PageArray"] = {:id => "PageArray", :properties => {:pages => {:type => "Array", :items =>{:$ref => "Page"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def pages
  return
end

##~ a = source2swagger.namespace("music")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/artists", :description => "Get music artists", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get music artists", :responseClass => "ArtistArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"

##~ a.models["Artist"] = {:id => "Artist", :properties => {:name => {:type => "string"}, :genre => {:type => "string"}}}
##~ a.models["ArtistArray"] = {:id => "ArtistArray", :properties => {:chapters => {:type => "Array", :items =>{:$ref => "Artist"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def artists
  return
end


##~ a = source2swagger.namespace("music")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/songs", :description => "Get songs by artist", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get songs by artist", :responseClass => "SongArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "artist_slug", :description => "artist slug", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "song_slug", :description => "get song by song slug", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"


##~ a.models["Lyric"] = {:id => "Lyric", :properties => {:artist_id => {:type => "int"}, :song_id => {:type => "int"},:lyrics => {:type => "string"}}}
##~ a.models["Image"] = {:id => "Image", :properties => {:artist_id => {:type => "int"}, :song_id => {:type => "int"},:image_url => {:type => "string"}}}
##~ a.models["Video"] = {:id => "Video", :properties => {:artist_id => {:type => "int"}, :song_id => {:type => "int"},:video_url => {:type => "string"}}}
##~ a.models["Chord"] = {:id => "Chord", :properties => {:artist_id => {:type => "int"}, :song_id => {:type => "int"},:instrument_code => {:type => "string"},:chords => {:type => "string"},:chords_url => {:type => "string"}}}
##~ a.models["Song"] = {:id => "Song", :properties => {:artist => {:type => "string"}, :title => {:type => "string"},:genre => {:type => "string"},:videos => {:type => "Array", :items =>{:$ref => "Video"}},:images => {:type => "Array", :items =>{:$ref => "Image"}},:lyrics => {:type => "Array", :items =>{:$ref => "Lyric"}},:chords => {:type => "Array", :items =>{:$ref => "Chord"} }}}
##~ a.models["SongArray"] = {:id => "SongArray", :properties => {:chapters => {:type => "Array", :items =>{:$ref => "Song"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def chapters
  return
end

##~ a = source2swagger.namespace("recipes")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/categories", :description => "Get Recipe Categories by language", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Categories", :responseClass => "CategoryArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "category_slug", :description => "get subcategories for category slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Category"] = {:id => "Category", :properties => {:name => {:type => "string"}, :parent => {:type => "string"}}}
##~ a.models["CategoryArray"] = {:id => "CategoryArray", :properties => {:categories => {:type => "Array", :items =>{:$ref => "Category"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def categories
  return
end


##~ a = source2swagger.namespace("recipes")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/recipe", :description => "Get recipes by slug or by category", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Recipe", :responseClass => "RecipeArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "recipe_slug", :description => "recipe slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"
##~ o.parameters.add :name => "category_slug", :description => "get recipes for category", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Recipe"] = {:id => "Recipe", :properties => {:title => {:type => "string"}, :instructions => {:type => "string"},:preparation_time => {:type => "integer"} , :ingredients => {:type => "Array", :items =>{:$ref => "string"} }}}
##~ a.models["RecipeArray"] = {:id => "RecipeArray", :properties => {:recipes => {:type => "Array", :items =>{:$ref => "Recipe"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def recipes
  return
end

##~ a = source2swagger.namespace("news")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/news", :description => "Get news array", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get News Feed", :responseClass => "NewsArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "news_slug", :description => "news slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"
##~ o.parameters.add :name => "category_slug", :description => "get news for category slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["News"] = {:id => "News", :properties => {:title => {:type => "string"}, :content => {:type => "string"},:url_reference => {:type => "string"}}}
##~ a.models["NewsArray"] = {:id => "NewsArray", :properties => {:news => {:type => "Array", :items =>{:$ref => "News"} }}}

##~ err = o.errorResponses.add
##~ err.set :reason => "Not found", :code => 404
##~ o.errorResponses.add :reason => "Invalid ID supplied", :code => 400
##~ o.errorResponses.add :reason => "Unprocessable Entity", :code => 422
##~ o.errorResponses.add :reason => "API Coming Soon", :code => 0
##~ o.errorResponses.add :reason => "Ok", :code => 200
def news
  return
end