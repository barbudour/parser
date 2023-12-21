# NumberExtensions.StoreAsync(INumberObject, INumberContext,
NumberLocationType, NumberStoreMode, CancellationToken) - метод
Сохраняет объект с номером в заданном местоположении и контексте.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> StoreAsync(
    	this INumberObject number,
    	INumberContext context,
    	NumberLocationType locationType,
    	NumberStoreMode storeMode = NumberStoreMode.WithNotification,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function StoreAsync ( 
    	number As INumberObject,
    	context As INumberContext,
    	locationType As NumberLocationType,
    	Optional storeMode As NumberStoreMode = NumberStoreMode.WithNotification,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<bool> StoreAsync(
    	INumberObject^ number, 
    	INumberContext^ context, 
    	NumberLocationType^ locationType, 
    	NumberStoreMode storeMode = NumberStoreMode::WithNotification, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member StoreAsync : 
            number : INumberObject * 
            context : INumberContext * 
            locationType : NumberLocationType * 
            ?storeMode : NumberStoreMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _storeMode = defaultArg storeMode NumberStoreMode.WithNotification
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
    Сохраняемый объект с номером.
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
locationType
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm)
     Тип местоположения номера для сохранения. Свойство типа [HasInfo](P_Tessa_Cards_Numbers_NumberLocationType_HasInfo.htm) должно возвращать false. 
storeMode [NumberStoreMode](T_Tessa_Cards_Numbers_NumberStoreMode.htm)
(Optional)
    Способ сохранения номера в карточке.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если текущий номер был успешно сохранён в местоположении locationType;
false, если возникла ошибка.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_Numbers_NumberExtensions_StoreAsync.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
