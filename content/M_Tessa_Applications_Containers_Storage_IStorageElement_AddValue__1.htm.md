# IStorageElement.AddValue<TValue>(String, TValue) - метод
Добавляет значение value текущий элемент
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void AddValue<TValue>(
    	[NotNullAttribute] string name,
    	TValue value
    )
    where TValue : struct, new()
VB __Копировать
     Sub AddValue(Of TValue As {Structure, New}) ( 
    	<NotNullAttribute> name As String,
    	value As TValue
    )
C++ __Копировать
    generic<typename TValue>
    where TValue : value class, gcnew()
    void AddValue(
    	[NotNullAttribute] String^ name, 
    	TValue value
    )
F# __Копировать
     abstract AddValue : 
            [<NotNullAttribute>] name : string * 
            value : 'TValue -> unit  when 'TValue : struct, new()
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя параметра 
value TValue
     Значение 
#### Параметры типа
TValue
     Значение объекта 
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Имя объекта является null  
---|---  
## __См. также
#### Ссылки
[IStorageElement -
](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
[AddValue -
перегрузка](Overload_Tessa_Applications_Containers_Storage_IStorageElement_AddValue.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
