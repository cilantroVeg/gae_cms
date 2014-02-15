# source2swagger -i /Users/arturo/interpegasus/gae_cms/projects/cms/static/template/API/specs/api-spec -e "rb" -c "##~" -o /Users/arturo/interpegasus/gae_cms/projects/cms/static/template/API/api-docs
# find ./ -name "*.json" -exec sh -c 'mv $0 `basename "$0" .json`' '{}' \;


##~ a = source2swagger.namespace("InterPegasus CMS API")
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


##~ a = source2swagger.namespace("InterPegasus CMS API")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/categories", :description => "Get CMS Categories by language", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Categories", :responseClass => "CategoryArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"

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


##~ a = source2swagger.namespace("InterPegasus CMS API")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/pages", :description => "Get pages by slug or by category", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Page", :responseClass => "PageArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "slug", :description => "page slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"
##~ o.parameters.add :name => "category", :description => "category name", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

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


##~ a = source2swagger.namespace("InterPegasus CMS API")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/images", :description => "Get images by slug or by category", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Image", :responseClass => "ImageArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "language_code", :description => "language code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "page", :description => "page slug", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"
##~ o.parameters.add :name => "category", :description => "category name", :dataType => "string", :allowMultiple => false, :required => false, :paramType => "query"

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


##~ a = source2swagger.namespace("Bible")
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

##~ a = source2swagger.namespace("Bible")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/chapters", :description => "Get chapters by book", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Bible Chapters by book", :responseClass => "ChapterArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "book_code", :description => "book code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "chapter_number", :description => "Chapter Number", :dataType => "int", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Chapter"] = {:id => "Chapter", :properties => {:title => {:type => "string"}, :content => {:type => "string"}}}
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

##~ a = source2swagger.namespace("NRWL")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/chapters", :description => "Get chapters by book", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Bible Chapters by book", :responseClass => "ChapterArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "book_code", :description => "book code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "chapter_number", :description => "Chapter Number", :dataType => "int", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Chapter"] = {:id => "Chapter", :properties => {:title => {:type => "string"}, :content => {:type => "string"}}}
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

##~ a = source2swagger.namespace("Music")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/chapters", :description => "Get chapters by book", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Bible Chapters by book", :responseClass => "ChapterArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "book_code", :description => "book code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "chapter_number", :description => "Chapter Number", :dataType => "int", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Chapter"] = {:id => "Chapter", :properties => {:title => {:type => "string"}, :content => {:type => "string"}}}
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

##~ a = source2swagger.namespace("Recipes")
##~ a.set "basePath" => "http://www.interpegasus.com/api", "swaggerVersion" => "1", "apiVersion" => "1.0"

##~ e = a.apis.add
##~ e.set :path => "/{language_code}/chapters", :description => "Get chapters by book", :format => "json"

##~ o = e.operations.add
##~ o.set :httpMethod => "GET", :summary => "Get Bible Chapters by book", :responseClass => "ChapterArray", :nickname => "pegasus", :tags => ["pegasus"], :deprecated => false
##~ o.parameters.add :name => "access_token", :description => "access_token", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "query"
##~ o.parameters.add :name => "book_code", :description => "book code", :dataType => "string", :allowMultiple => false, :required => true, :paramType => "path"
##~ o.parameters.add :name => "chapter_number", :description => "Chapter Number", :dataType => "int", :allowMultiple => false, :required => false, :paramType => "query"

##~ a.models["Chapter"] = {:id => "Chapter", :properties => {:title => {:type => "string"}, :content => {:type => "string"}}}
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

