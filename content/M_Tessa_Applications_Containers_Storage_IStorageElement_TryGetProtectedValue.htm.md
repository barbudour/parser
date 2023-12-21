# IStorageElement.TryGetProtectedValue - метод
Возвращает значение для имени name из текущего элемента name. Расшифровывая
содержимое элемента. Если значение отсутствует в элементе будет возвращено
null.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    string TryGetProtectedValue(
    	[NotNullAttribute] string name
    )
VB __Копировать
    <CanBeNullAttribute>
    Function TryGetProtectedValue ( 
    	<NotNullAttribute> name As String
    ) As String
C++ __Копировать
    [CanBeNullAttribute]
    String^ TryGetProtectedValue(
    	[NotNullAttribute] String^ name
    )
F# __Копировать
     [<CanBeNullAttribute>]
    abstract TryGetProtectedValue : 
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
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
