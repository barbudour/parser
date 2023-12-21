# NumberDirector.NotifyOnDeletingBackupCardAsync - метод
Уведомляет о том, что карточка окончательно удаляется, т.е. удаляется её
удалённая карточка [Tessa.Cards.CardHelper.DeletedTypeName]. При этом может
потребоваться освободить занятый номер. Обычно выполняется на этапе
BeforeCommitTransaction при удалении удалённой карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> NotifyOnDeletingBackupCardAsync(
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function NotifyOnDeletingBackupCardAsync ( 
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ NotifyOnDeletingBackupCardAsync(
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract NotifyOnDeletingBackupCardAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override NotifyOnDeletingBackupCardAsync : 
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
[INumberDirector.NotifyOnDeletingBackupCardAsync(INumberContext,
CancellationToken)](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnDeletingBackupCardAsync.htm)  
##  __См. также
#### Ссылки
[NumberDirector - ](T_Tessa_Cards_Numbers_NumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
