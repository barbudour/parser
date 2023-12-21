# NumberControlRequestExtension.CreateResponseAsync - метод
Создаёт объект ответа на запрос для успешно выполненного действия с номером.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<NumberControlResponse> CreateResponseAsync(
    	ICardRequestExtensionContext context,
    	NumberControlRequest request,
    	INumberContext numberContext,
    	INumberLocation numberLocation,
    	NumberTypeDescriptor numberType
    )
VB __Копировать
     Protected Overridable Function CreateResponseAsync ( 
    	context As ICardRequestExtensionContext,
    	request As NumberControlRequest,
    	numberContext As INumberContext,
    	numberLocation As INumberLocation,
    	numberType As NumberTypeDescriptor
    ) As ValueTask(Of NumberControlResponse)
C++ __Копировать
     protected:
    virtual ValueTask<NumberControlResponse^> CreateResponseAsync(
    	ICardRequestExtensionContext^ context, 
    	NumberControlRequest^ request, 
    	INumberContext^ numberContext, 
    	INumberLocation^ numberLocation, 
    	NumberTypeDescriptor^ numberType
    )
F# __Копировать
     abstract CreateResponseAsync : 
            context : ICardRequestExtensionContext * 
            request : NumberControlRequest * 
            numberContext : INumberContext * 
            numberLocation : INumberLocation * 
            numberType : NumberTypeDescriptor -> ValueTask<NumberControlResponse> 
    override CreateResponseAsync : 
            context : ICardRequestExtensionContext * 
            request : NumberControlRequest * 
            numberContext : INumberContext * 
            numberLocation : INumberLocation * 
            numberType : NumberTypeDescriptor -> ValueTask<NumberControlResponse> 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст выполнения расширений.
request [NumberControlRequest](T_Tessa_Cards_Numbers_NumberControlRequest.htm)
    Запрос на выполнение действий с номерами.
numberContext [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberLocation [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
    Местоположение номера, с которым работает элемент управления.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Информация по типу номера, с которым работает элемент управления.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[NumberControlResponse](T_Tessa_Cards_Numbers_NumberControlResponse.htm)>  
Созданный ответ на запрос для успешно выполненного действия с номером.
##  __См. также
#### Ссылки
[NumberControlRequestExtension -
](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
