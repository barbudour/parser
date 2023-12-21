# IStorageElement.TryGetValue(String) - метод
Возвращает значение для имени name из текущего элемента name. Если значение
отсутствует в элементе будет возвращено null.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    string TryGetValue(
    	[NotNullAttribute] string name
    )
VB __Копировать
    <CanBeNullAttribute>
    Function TryGetValue ( 
    	<NotNullAttribute> name As String
    ) As String
C++ __Копировать
    [CanBeNullAttribute]
    String^ TryGetValue(
    	[NotNullAttribute] String^ name
    )
F# __Копировать
     [<CanBeNullAttribute>]
    abstract TryGetValue : 
            [<NotNullAttribute>] name : string -> string 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя значения 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Результат получения значения
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Имя объекта является null  
---|---  
## __См. также
#### Ссылки
[IStorageElement -
](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
[TryGetValue -
перегрузка](Overload_Tessa_Applications_Containers_Storage_IStorageElement_TryGetValue.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
