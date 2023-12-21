# CardHelper.ParseMergeOptionsAsync - метод
Загружает опции слияния из файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ICardMergeOptions> ParseMergeOptionsAsync(
    	ISourceContentProvider optionsFileProvider,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function ParseMergeOptionsAsync ( 
    	optionsFileProvider As ISourceContentProvider,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardMergeOptions)
C++ __Копировать
     public:
    static Task<ICardMergeOptions^>^ ParseMergeOptionsAsync(
    	ISourceContentProvider^ optionsFileProvider, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member ParseMergeOptionsAsync : 
            optionsFileProvider : ISourceContentProvider * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardMergeOptions> 
#### Параметры
optionsFileProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для файла опций слияния.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardMergeOptions](T_Tessa_Cards_SmartMerge_ICardMergeOptions.htm)>  
Объект опций слияния типа
[ICardMergeOptions](T_Tessa_Cards_SmartMerge_ICardMergeOptions.htm).
##  __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Невозможно загрузить или десериализовать опции. Причина ошибки во внутреннем
исключении.  
---|---  
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
