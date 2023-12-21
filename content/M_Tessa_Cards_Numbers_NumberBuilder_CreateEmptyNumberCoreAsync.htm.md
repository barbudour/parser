# NumberBuilder.CreateEmptyNumberCoreAsync - метод
Создаёт объект, описывающий пустой номер заданного типа. Возвращённое значение
не может быть равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<INumberObject> CreateEmptyNumberCoreAsync(
    	NumberTypeDescriptor numberType,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function CreateEmptyNumberCoreAsync ( 
    	numberType As NumberTypeDescriptor,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     protected:
    virtual ValueTask<INumberObject^> CreateEmptyNumberCoreAsync(
    	NumberTypeDescriptor^ numberType, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateEmptyNumberCoreAsync : 
            numberType : NumberTypeDescriptor * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
    override CreateEmptyNumberCoreAsync : 
            numberType : NumberTypeDescriptor * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
#### Параметры
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация по номеру или null, если такая информация отсутствует. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Объект, описывающий пустой номер заданного типа.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
