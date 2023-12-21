# IStorageElement.GetProtectedValue - метод
Возвращает значение для имени name из текущего элемента name. Содержимое будет
расшифровано Если значение отсутствует в элементе будет выдано исключение
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    string GetProtectedValue(
    	[NotNullAttribute] string name
    )
VB __Копировать
    <NotNullAttribute>
    Function GetProtectedValue ( 
    	<NotNullAttribute> name As String
    ) As String
C++ __Копировать
    [NotNullAttribute]
    String^ GetProtectedValue(
    	[NotNullAttribute] String^ name
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract GetProtectedValue : 
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
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)|
Значение для объекта не найдено в текущем элементе
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)  
##  __См. также
#### Ссылки
[IStorageElement -
](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
