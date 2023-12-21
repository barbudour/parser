# IStorageElement.GetValue<TValue>(String) - метод
Возвращает значение для имени name из текущего элемента name. Если значение
отсутствует в элементе будет выдано исключение
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     TValue GetValue<TValue>(
    	[NotNullAttribute] string name
    )
    where TValue : struct, new()
VB __Копировать
     Function GetValue(Of TValue As {Structure, New}) ( 
    	<NotNullAttribute> name As String
    ) As TValue
C++ __Копировать
    generic<typename TValue>
    where TValue : value class, gcnew()
    TValue GetValue(
    	[NotNullAttribute] String^ name
    )
F# __Копировать
     abstract GetValue : 
            [<NotNullAttribute>] name : string -> 'TValue  when 'TValue : struct, new()
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя значения 
#### Параметры типа
TValue
     Тип элемента 
#### Возвращаемое значение
TValue  
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
[GetValue -
перегрузка](Overload_Tessa_Applications_Containers_Storage_IStorageElement_GetValue.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
