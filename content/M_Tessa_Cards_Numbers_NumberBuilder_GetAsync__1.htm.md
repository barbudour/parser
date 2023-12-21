# NumberBuilder.GetAsync<T> \- метод
Возвращает типизированные данные для контекста события, происходящего с
номером.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<T> GetAsync<T>(
    	INumberContext context,
    	Object parameter = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsync(Of T) ( 
    	context As INumberContext,
    	Optional parameter As Object = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of T)
C++ __Копировать
     public:
    generic<typename T>
    virtual ValueTask<T> GetAsync(
    	INumberContext^ context, 
    	Object^ parameter = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAsync : 
            context : INumberContext * 
            ?parameter : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parameter = defaultArg parameter null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
    override GetAsync : 
            context : INumberContext * 
            ?parameter : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parameter = defaultArg parameter null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
parameter [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
    Необязательный параметр, определяющий запрашиваемые данные.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
T
    Тип запрашиваемых данных.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<T>  
Запрошенные типизированные данные для контекста события, происходящего с
номером, или null, если получить такие данные не удалось.
#### Реализации
[INumberBuilder.GetAsync<T>(INumberContext, Object,
CancellationToken)](M_Tessa_Cards_Numbers_INumberBuilder_GetAsync__1.htm)  
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
