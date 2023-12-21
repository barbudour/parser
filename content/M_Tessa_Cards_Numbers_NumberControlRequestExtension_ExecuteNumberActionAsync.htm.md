# NumberControlRequestExtension.ExecuteNumberActionAsync - метод
Выполняет действие с номером для заданного контекста. Возвращает признак того,
что действие успешно выполнено.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<bool> ExecuteNumberActionAsync(
    	ICardRequestExtensionContext context,
    	NumberControlRequest request,
    	INumberContext numberContext,
    	INumberDirector numberDirector
    )
VB __Копировать
     Protected MustOverride Function ExecuteNumberActionAsync ( 
    	context As ICardRequestExtensionContext,
    	request As NumberControlRequest,
    	numberContext As INumberContext,
    	numberDirector As INumberDirector
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ ExecuteNumberActionAsync(
    	ICardRequestExtensionContext^ context, 
    	NumberControlRequest^ request, 
    	INumberContext^ numberContext, 
    	INumberDirector^ numberDirector
    ) abstract
F# __Копировать
     abstract ExecuteNumberActionAsync : 
            context : ICardRequestExtensionContext * 
            request : NumberControlRequest * 
            numberContext : INumberContext * 
            numberDirector : INumberDirector -> Task<bool> 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст выполнения расширений.
request [NumberControlRequest](T_Tessa_Cards_Numbers_NumberControlRequest.htm)
    Запрос на выполнение действий с номерами.
numberContext [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberDirector [INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm)
    Объект, выполняющий действие в API номеров.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если действие с номером было успешно выполнено; false в противном
случае.
## __См. также
#### Ссылки
[NumberControlRequestExtension -
](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
