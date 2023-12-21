# NumberBuilder.CreateNumberCoreAsync - метод
Создаёт объект, описывающий номер с заданными параметрами. Номер может быть
пустым или не пустым в зависимости от параметров. Возвращённое значение не
может быть равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<INumberObject> CreateNumberCoreAsync(
    	long? number,
    	string fullNumber,
    	string sequenceName,
    	NumberTypeDescriptor numberType,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function CreateNumberCoreAsync ( 
    	number As Long?,
    	fullNumber As String,
    	sequenceName As String,
    	numberType As NumberTypeDescriptor,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     protected:
    virtual ValueTask<INumberObject^> CreateNumberCoreAsync(
    	Nullable<long long> number, 
    	String^ fullNumber, 
    	String^ sequenceName, 
    	NumberTypeDescriptor^ numberType, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateNumberCoreAsync : 
            number : Nullable<int64> * 
            fullNumber : string * 
            sequenceName : string * 
            numberType : NumberTypeDescriptor * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
    override CreateNumberCoreAsync : 
            number : Nullable<int64> * 
            fullNumber : string * 
            sequenceName : string * 
            numberType : NumberTypeDescriptor * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
#### Параметры
number
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
     Числовое представление номера. Может быть равно null. 
fullNumber [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строковое представление номера. Может быть равно null или пустой строке. 
sequenceName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя последовательности, из которой был выделен или будет выделен номер.
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
Объект, описывающий номер с заданными параметрами.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
