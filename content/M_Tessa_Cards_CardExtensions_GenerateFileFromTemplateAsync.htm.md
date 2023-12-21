# CardExtensions.GenerateFileFromTemplateAsync(ICardStreamClientRepository,
Guid, Nullable<Guid>, Func<Stream, CancellationToken, ValueTask>,
IViewPlaceholderContext, Dictionary<String, Object>, CancellationToken) -
метод
Создаёт файл по заданному шаблону и возвращает контент созданного файла и
ответ на запрос на создание.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<CardGetFileContentResponse> GenerateFileFromTemplateAsync(
    	this ICardStreamClientRepository repository,
    	Guid templateID,
    	Guid? cardID,
    	Func<Stream, CancellationToken, ValueTask> processContentActionAsync,
    	IViewPlaceholderContext viewPlaceholderContext = null,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GenerateFileFromTemplateAsync ( 
    	repository As ICardStreamClientRepository,
    	templateID As Guid,
    	cardID As Guid?,
    	processContentActionAsync As Func(Of Stream, CancellationToken, ValueTask),
    	Optional viewPlaceholderContext As IViewPlaceholderContext = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetFileContentResponse)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<CardGetFileContentResponse^>^ GenerateFileFromTemplateAsync(
    	ICardStreamClientRepository^ repository, 
    	Guid templateID, 
    	Nullable<Guid> cardID, 
    	Func<Stream^, CancellationToken, ValueTask>^ processContentActionAsync, 
    	IViewPlaceholderContext^ viewPlaceholderContext = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GenerateFileFromTemplateAsync : 
            repository : ICardStreamClientRepository * 
            templateID : Guid * 
            cardID : Nullable<Guid> * 
            processContentActionAsync : Func<Stream, CancellationToken, ValueTask> * 
            ?viewPlaceholderContext : IViewPlaceholderContext * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _viewPlaceholderContext = defaultArg viewPlaceholderContext null
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetFileContentResponse> 
#### Параметры
repository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
    Репозиторий для получения контента на клиенте.
templateID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки шаблона файла.
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор карточки, используемый в плейсхолдерах шаблона, или null, если шаблон создаётся без привязки к карточке. 
processContentActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
     Метод, выполняющий чтение и обработку контента версии файла. Метод не вызывается, если контент файла не был передан. 
viewPlaceholderContext
[IViewPlaceholderContext](T_Tessa_Platform_Placeholders_IViewPlaceholderContext.htm)
(Optional)
     Контекст плейсхолдеров для представлений или null, если шаблон создаётся без привязки к представлению. 
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, передаваемая в запрос на получение контента файла, или null, если дополнительная информация не передаётся. Информация будет доступна из контекста плейсхолдера по тем же ключам, которые заданы в параметре, например: context.Info["Key"]. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
     Объект, посредством которого можно отменить выполнение запроса с клиента на сервер. Укажите значение по умолчанию CancellationToken.None, если отмена не требуется. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)>  
Ответ на запрос на получение контента файла, созданного по шаблону.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[GenerateFileFromTemplateAsync -
перегрузка](Overload_Tessa_Cards_CardExtensions_GenerateFileFromTemplateAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
