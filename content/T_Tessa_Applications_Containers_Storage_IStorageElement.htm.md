# IStorageElement - интерфейс
Описание интерфейса элемента хранилища
[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStorageElement : IDisposable, 
    	IComposite<IStorageElement, IStorageElementOperationVisitor>, IComponent<IStorageElementOperationVisitor>, 
    	IComponent
VB __Копировать
     Public Interface IStorageElement
    	Inherits IDisposable, IComposite(Of IStorageElement, IStorageElementOperationVisitor), 
    	IComponent(Of IStorageElementOperationVisitor), IComponent
C++ __Копировать
     public interface class IStorageElement : IDisposable, 
    	IComposite<IStorageElement^, IStorageElementOperationVisitor^>, IComponent<IStorageElementOperationVisitor^>, 
    	IComponent
F# __Копировать
     type IStorageElement = 
        interface
            interface IDisposable
            interface IComposite<IStorageElement, IStorageElementOperationVisitor>
            interface IComponent<IStorageElementOperationVisitor>
            interface IComponent
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IComponent](T_Tessa_Applications_Containers_IComponent.htm), [IComponent](T_Tessa_Applications_Containers_IComponent_1.htm)<[IStorageElementOperationVisitor](T_Tessa_Applications_Containers_Storage_IStorageElementOperationVisitor.htm)>, [IComposite](T_Tessa_Applications_Containers_IComposite_2.htm)<IStorageElement, [IStorageElementOperationVisitor](T_Tessa_Applications_Containers_Storage_IStorageElementOperationVisitor.htm)>
##  __Свойства
[Components](P_Tessa_Applications_Containers_IComposite_2_Components.htm)|
Gets Возвращает список компонентов контейнера расположенных непосредственно в
самом контейнере.  
(Унаследован от [IComposite<TComponent,
TOperation>](T_Tessa_Applications_Containers_IComposite_2.htm))  
---|---  
[Elements](P_Tessa_Applications_Containers_Storage_IStorageElement_Elements.htm)|
Gets Возвращает список дочерних элементов  
[Name](P_Tessa_Applications_Containers_Storage_IStorageElement_Name.htm)|
Gets Имя элемента  
[Parent](P_Tessa_Applications_Containers_IComponent_Parent.htm)|  Gets or sets
Родитель/Владелец  
(Унаследован от [IComponent](T_Tessa_Applications_Containers_IComponent.htm))  
##  __Методы
[Accept](M_Tessa_Applications_Containers_IComponent_1_Accept.htm)|  Вызывает
выполнение операции operation над текущим узлом  
(Унаследован от
[IComponent<TOperation>](T_Tessa_Applications_Containers_IComponent_1.htm))  
---|---  
[AddComponent](M_Tessa_Applications_Containers_IComposite_2_AddComponent.htm)|
Добавляет компонент component в контейнер. Добавляемый компонент должен быть
не равен null.  
(Унаследован от [IComposite<TComponent,
TOperation>](T_Tessa_Applications_Containers_IComposite_2.htm))  
[AddProtectedValue](M_Tessa_Applications_Containers_Storage_IStorageElement_AddProtectedValue.htm)|
Добавляет значение value содержащее строку в текущий элемент IStorageElement.
зашифровывая содержимое  
[AddValue(String,
String)](M_Tessa_Applications_Containers_Storage_IStorageElement_AddValue.htm)|
Добавляет значение value содержащее строку в текущий элемент IStorageElement.  
[AddValue<TValue>(String,
TValue)](M_Tessa_Applications_Containers_Storage_IStorageElement_AddValue__1.htm)|
Добавляет значение value текущий элемент IStorageElement.  
[ClearComponents](M_Tessa_Applications_Containers_IComposite_2_ClearComponents.htm)|
Осуществляет удаление из контейнера всех элементов  
(Унаследован от [IComposite<TComponent,
TOperation>](T_Tessa_Applications_Containers_IComposite_2.htm))  
[CreateElement](M_Tessa_Applications_Containers_Storage_IStorageElement_CreateElement.htm)|
Осуществляет создание элемента хранилища IStorageElement с именем name  
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
[GetFullyQualifiedName](M_Tessa_Applications_Containers_IComponent_GetFullyQualifiedName.htm)|
Возвращает полное имя объекта  
(Унаследован от [IComponent](T_Tessa_Applications_Containers_IComponent.htm))  
[GetProtectedValue](M_Tessa_Applications_Containers_Storage_IStorageElement_GetProtectedValue.htm)|
Возвращает значение для имени name из текущего элемента name. Содержимое будет
расшифровано Если значение отсутствует в элементе будет выдано исключение
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)  
[GetValue(String)](M_Tessa_Applications_Containers_Storage_IStorageElement_GetValue.htm)|
Возвращает значение для имени name из текущего элемента name. Если значение
отсутствует в элементе будет выдано исключение
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)  
[GetValue<TValue>(String)](M_Tessa_Applications_Containers_Storage_IStorageElement_GetValue__1.htm)|
Возвращает значение для имени name из текущего элемента name. Если значение
отсутствует в элементе будет выдано исключение
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)  
[RemoveComponent](M_Tessa_Applications_Containers_IComposite_2_RemoveComponent.htm)|
Удаляет компонент component из контейнера. Удаляемый компонент должен быть не
равен null  
(Унаследован от [IComposite<TComponent,
TOperation>](T_Tessa_Applications_Containers_IComposite_2.htm))  
[TryGetProtectedValue](M_Tessa_Applications_Containers_Storage_IStorageElement_TryGetProtectedValue.htm)|
Возвращает значение для имени name из текущего элемента name. Расшифровывая
содержимое элемента. Если значение отсутствует в элементе будет возвращено
null.  
[TryGetValue(String)](M_Tessa_Applications_Containers_Storage_IStorageElement_TryGetValue.htm)|
Возвращает значение для имени name из текущего элемента name. Если значение
отсутствует в элементе будет возвращено null.  
[TryGetValue<TValue>(String)](M_Tessa_Applications_Containers_Storage_IStorageElement_TryGetValue__1.htm)|
Возвращает значение для имени name из текущего элемента name. Если значение
отсутствует в элементе будет возвращено null.  
## __Методы расширения
[GetElements](M_Tessa_Applications_Containers_Storage_StorageExtender_GetElements_1.htm)|
Возвращает список дочерних элементов элемента element с именем name  
(Определяется
[StorageExtender](T_Tessa_Applications_Containers_Storage_StorageExtender.htm))  
---|---  
[GetElements](M_Tessa_Applications_Containers_Storage_StorageExtender_GetElements.htm)|
Возвращает список элементов находящихся вниз по иерархическому пути path от
элемента element  
(Определяется
[StorageExtender](T_Tessa_Applications_Containers_Storage_StorageExtender.htm))  
[GetElements](M_Tessa_Applications_Containers_Storage_StorageExtender_GetElements_2.htm)|
Возвращает список дочерних элементов элемента element с именем name  
(Определяется
[StorageExtender](T_Tessa_Applications_Containers_Storage_StorageExtender.htm))  
[TryGetElement](M_Tessa_Applications_Containers_Storage_StorageExtender_TryGetElement.htm)|
Возвращает первый элемент из списка дочерних элементов element с именем name
или null, если элемент отсутствует в списке  
(Определяется
[StorageExtender](T_Tessa_Applications_Containers_Storage_StorageExtender.htm))  
[TryGetElement](M_Tessa_Applications_Containers_Storage_StorageExtender_TryGetElement_1.htm)|
Возвращает первый элемент из списка дочерних элементов element с именем name
или null, если элемент отсутствует в списке  
(Определяется
[StorageExtender](T_Tessa_Applications_Containers_Storage_StorageExtender.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
