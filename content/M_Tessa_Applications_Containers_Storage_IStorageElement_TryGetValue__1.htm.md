# IStorageElement.TryGetValue<TValue>(String) - метод
Возвращает значение для имени name из текущего элемента name. Если значение
отсутствует в элементе будет возвращено null.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    TValue? TryGetValue<TValue>(
    	[NotNullAttribute] string name
    )
    where TValue : struct, new()
VB __Копировать
    <CanBeNullAttribute>
    Function TryGetValue(Of TValue As {Structure, New}) ( 
    	<NotNullAttribute> name As String
    ) As TValue?
C++ __Копировать
    [CanBeNullAttribute]
    generic<typename TValue>
    where TValue : value class, gcnew()
    Nullable<TValue> TryGetValue(
    	[NotNullAttribute] String^ name
    )
F# __Копировать
     [<CanBeNullAttribute>]
    abstract TryGetValue : 
            [<NotNullAttribute>] name : string -> Nullable<'TValue>  when 'TValue : struct, new()
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя значения 
#### Параметры типа
TValue
     Тип значения 
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<TValue>  
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
