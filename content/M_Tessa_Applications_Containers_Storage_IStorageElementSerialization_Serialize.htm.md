# IStorageElementSerialization.Serialize - метод
Осущестляет запись свойств объекта в элемент container
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void Serialize(
    	[NotNullAttribute] IStorageElement container
    )
VB __Копировать
     Sub Serialize ( 
    	<NotNullAttribute> container As IStorageElement
    )
C++ __Копировать
     void Serialize(
    	[NotNullAttribute] IStorageElement^ container
    )
F# __Копировать
     abstract Serialize : 
            [<NotNullAttribute>] container : IStorageElement -> unit 
#### Параметры
container
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
     Контейнер в который необходимо добавить сериализуемые элементы. Как правило класс реализующий данный интерфейс использует данный параметр в качестве контейнера и добавляет в него свои дочерние элементы типа [IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
##  __Исключения
[SerializationException](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationexception)|
Ошибки сериализации  
---|---  
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
В качестве контейнера container был передан null  
## __См. также
#### Ссылки
[IStorageElementSerialization -
](T_Tessa_Applications_Containers_Storage_IStorageElementSerialization.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
