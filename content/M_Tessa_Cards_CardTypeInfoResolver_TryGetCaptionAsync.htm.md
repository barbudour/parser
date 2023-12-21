# CardTypeInfoResolver.TryGetCaptionAsync - метод
Возвращает отображаемое имя типа карточки или null, если тип карточки не
найден. Возвращённое значение может быть строкой локализации.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<string> TryGetCaptionAsync(
    	Guid typeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetCaptionAsync ( 
    	typeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    virtual ValueTask<String^> TryGetCaptionAsync(
    	Guid typeID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetCaptionAsync : 
            typeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
    override TryGetCaptionAsync : 
            typeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
typeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Отображаемое имя типа карточки или null, если тип карточки не найден.
#### Реализации
[ITypeInfoResolver.TryGetCaptionAsync(Guid,
CancellationToken)](M_Tessa_Platform_Runtime_ITypeInfoResolver_TryGetCaptionAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeInfoResolver - ](T_Tessa_Cards_CardTypeInfoResolver.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
