# CardExtensions.GenerateFileFromTemplateAsync(ICardStreamServerRepository,
Guid, Nullable<Guid>, IViewPlaceholderContext, Dictionary<String, Object>,
CancellationToken) - метод
Асинхронно создаёт файл по заданному шаблону и возвращает контент созданного
файла и ответ на запрос на создание.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ICardFileContentResult> GenerateFileFromTemplateAsync(
    	this ICardStreamServerRepository repository,
    	Guid templateID,
    	Guid? cardID,
    	IViewPlaceholderContext viewPlaceholderContext = null,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GenerateFileFromTemplateAsync ( 
    	repository As ICardStreamServerRepository,
    	templateID As Guid,
    	cardID As Guid?,
    	Optional viewPlaceholderContext As IViewPlaceholderContext = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardFileContentResult)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<ICardFileContentResult^>^ GenerateFileFromTemplateAsync(
    	ICardStreamServerRepository^ repository, 
    	Guid templateID, 
    	Nullable<Guid> cardID, 
    	IViewPlaceholderContext^ viewPlaceholderContext = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GenerateFileFromTemplateAsync : 
            repository : ICardStreamServerRepository * 
            templateID : Guid * 
            cardID : Nullable<Guid> * 
            ?viewPlaceholderContext : IViewPlaceholderContext * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _viewPlaceholderContext = defaultArg viewPlaceholderContext null
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardFileContentResult> 
#### Параметры
repository
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)
    Репозиторий для получения контента на клиенте.
templateID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки шаблона файла.
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор карточки, используемый в плейсхолдерах шаблона, или null, если шаблон создаётся без привязки к карточке. 
viewPlaceholderContext
[IViewPlaceholderContext](T_Tessa_Platform_Placeholders_IViewPlaceholderContext.htm)
(Optional)
     Контекст плейсхолдеров для представлений или null, если шаблон создаётся без привязки к представлению. 
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, передаваемая в запрос на получение контента файла, или null, если дополнительная информация не передаётся. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardFileContentResult](T_Tessa_Cards_ICardFileContentResult.htm)>  
Задача, возвращающая ответ на запрос на получение контента файла, созданного
по шаблону, и собственно сам контент файла.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm).
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
