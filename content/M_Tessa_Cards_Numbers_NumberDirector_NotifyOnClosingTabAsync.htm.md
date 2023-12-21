# NumberDirector.NotifyOnClosingTabAsync - метод
Уведомляет о том, что на стороне клиента закрывается вкладка с карточкой. При
этом может потребоваться освободить номер, если он был зарезервирован и ещё не
был занят.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> NotifyOnClosingTabAsync(
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function NotifyOnClosingTabAsync ( 
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ NotifyOnClosingTabAsync(
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract NotifyOnClosingTabAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override NotifyOnClosingTabAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если обработка события успешно выполнена; false, если обработка события
была отменена или при выполнении обработки возникли ошибки.
#### Реализации
[INumberDirector.NotifyOnClosingTabAsync(INumberContext,
CancellationToken)](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnClosingTabAsync.htm)  
##  __См. также
#### Ссылки
[NumberDirector - ](T_Tessa_Cards_Numbers_NumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
