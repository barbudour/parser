# NumberExtensions.GetNumberAsync(INumberLocationManager, INumberContext,
NumberTypeDescriptor, NumberLocationType, CancellationToken) - метод
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<INumberObject> GetNumberAsync(
    	this INumberLocationManager manager,
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	NumberLocationType locationType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetNumberAsync ( 
    	manager As INumberLocationManager,
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	locationType As NumberLocationType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<INumberObject^> GetNumberAsync(
    	INumberLocationManager^ manager, 
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	NumberLocationType^ locationType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetNumberAsync : 
            manager : INumberLocationManager * 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            locationType : NumberLocationType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
#### Параметры
manager
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm)
     Объект, определяющий поведение местоположения. В качестве такого объекта может использоваться [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm). 
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип получаемого номера.
locationType
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm)
     Тип местоположения получаемого номера. Свойство типа [HasInfo](P_Tessa_Cards_Numbers_NumberLocationType_HasInfo.htm) должно возвращать false. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Номер, расположенный в заданных местоположении и контексте или пустой номер,
если он не был найден. Метод не возвращает null.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[GetNumberAsync -
перегрузка](Overload_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
