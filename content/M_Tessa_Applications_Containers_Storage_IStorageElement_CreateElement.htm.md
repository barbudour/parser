# IStorageElement.CreateElement - метод
Осуществляет создание элемента хранилища
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
с именем name
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IStorageElement CreateElement(
    	[NotNullAttribute] string name
    )
VB __Копировать
    <NotNullAttribute>
    Function CreateElement ( 
    	<NotNullAttribute> name As String
    ) As IStorageElement
C++ __Копировать
    [NotNullAttribute]
    IStorageElement^ CreateElement(
    	[NotNullAttribute] String^ name
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract CreateElement : 
            [<NotNullAttribute>] name : string -> IStorageElement 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя элемента 
#### Возвращаемое значение
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)  
Возвращает созданный элемент
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
