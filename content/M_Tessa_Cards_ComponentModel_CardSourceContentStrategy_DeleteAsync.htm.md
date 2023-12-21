# CardSourceContentStrategy.DeleteAsync - метод
Удаляет контент версии файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteAsync(
    	CardContentContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteAsync ( 
    	context As CardContentContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteAsync(
    	CardContentContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteAsync : 
            context : CardContentContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteAsync : 
            context : CardContentContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
    Контекст, описывающий удаляемый контент версии файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardContentStrategy.DeleteAsync(CardContentContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardContentStrategy_DeleteAsync.htm)  
##  __См. также
#### Ссылки
[CardSourceContentStrategy -
](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
