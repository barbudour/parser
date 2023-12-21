# ApplicationPackage.Serialize(IStorageElement) - метод
Осуществляет запись свойств объекта в элемент container
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Serialize(
    	IStorageElement container
    )
VB __Копировать
     Public Sub Serialize ( 
    	container As IStorageElement
    )
C++ __Копировать
     public:
    virtual void Serialize(
    	IStorageElement^ container
    ) sealed
F# __Копировать
     abstract Serialize : 
            container : IStorageElement -> unit 
    override Serialize : 
            container : IStorageElement -> unit 
#### Параметры
container
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
     Контейнер в который необходимо добавить сериализуемые элементы. Как правило класс реализующий данный интерфейс использует данный параметр в качестве контейнера и добавляет в него свои дочерние элементы типа [IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
#### Реализации
[IStorageElementSerialization.Serialize(IStorageElement)](M_Tessa_Applications_Containers_Storage_IStorageElementSerialization_Serialize.htm)  
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
В качестве контейнера container был передан null  
---|---  
## __См. также
#### Ссылки
[ApplicationPackage - ](T_Tessa_Applications_Package_ApplicationPackage.htm)
[Serialize -
перегрузка](Overload_Tessa_Applications_Package_ApplicationPackage_Serialize.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
