# CardActionTextDescriptionBuilder.AppendLoginAsync - метод
Добавляет текст описания для записи в истории, которая относится к
выполненному входу в систему.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<StringBuilder> AppendLoginAsync(
    	StringBuilder builder,
    	Dictionary<string, Object> storage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function AppendLoginAsync ( 
    	builder As StringBuilder,
    	storage As Dictionary(Of String, Object),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of StringBuilder)
C++ __Копировать
     public:
    virtual ValueTask<StringBuilder^> AppendLoginAsync(
    	StringBuilder^ builder, 
    	Dictionary<String^, Object^>^ storage, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract AppendLoginAsync : 
            builder : StringBuilder * 
            storage : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<StringBuilder> 
    override AppendLoginAsync : 
            builder : StringBuilder * 
            storage : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<StringBuilder> 
#### Параметры
builder
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
    Объект, содержащий текстовое описание информации о записи в истории действий.
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище для записи в истории действий с информацией по выполненному входу в систему.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)>  
Объект builder для цепочки вызовов.
#### Реализации
[ICardActionDescriptionBuilder.AppendLoginAsync(StringBuilder,
Dictionary<String, Object>,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardActionDescriptionBuilder_AppendLoginAsync.htm)  
##  __См. также
#### Ссылки
[CardActionTextDescriptionBuilder -
](T_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
