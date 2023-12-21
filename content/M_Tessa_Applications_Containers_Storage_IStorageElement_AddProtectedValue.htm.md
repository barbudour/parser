# IStorageElement.AddProtectedValue - метод
Добавляет значение value содержащее строку в текущий элемент
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm).
зашифровывая содержимое
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void AddProtectedValue(
    	string name,
    	string value
    )
VB __Копировать
     Sub AddProtectedValue ( 
    	name As String,
    	value As String
    )
C++ __Копировать
     void AddProtectedValue(
    	String^ name, 
    	String^ value
    )
F# __Копировать
     abstract AddProtectedValue : 
            name : string * 
            value : string -> unit 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя параметра 
value [String](https://learn.microsoft.com/dotnet/api/system.string)
     Значение 
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Имя или значение объекта является null  
---|---  
## __См. также
#### Ссылки
[IStorageElement -
](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
