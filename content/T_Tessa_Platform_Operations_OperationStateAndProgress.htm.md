# OperationStateAndProgress - структура
Состояние операции совместно с её прогрессом.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public struct OperationStateAndProgress : IBinarySerializable, 
    	IStorageSerializable
VB __Копировать
    <SerializableAttribute>
    Public Structure OperationStateAndProgress
    	Implements IBinarySerializable, IStorageSerializable
C++ __Копировать
    [SerializableAttribute]
    public value class OperationStateAndProgress : IBinarySerializable, 
    	IStorageSerializable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type OperationStateAndProgress = 
        struct
            inherit ValueType
            interface IBinarySerializable
            interface IStorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ OperationStateAndProgress
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Конструкторы
[OperationStateAndProgress](M_Tessa_Platform_Operations_OperationStateAndProgress__ctor.htm)|
Создаёт экземпляр структуры с указанием её параметров.  
---|---  
## __Свойства
[Progress](P_Tessa_Platform_Operations_OperationStateAndProgress_Progress.htm)|
Прогресс операции в процентах, от 0 до 100, или null, если прогресс недоступен
для текущего состояния или операции в целом.  
---|---  
[State](P_Tessa_Platform_Operations_OperationStateAndProgress_State.htm)|
Текущее состояние операции.  
## __Методы
[Deconstruct](M_Tessa_Platform_Operations_OperationStateAndProgress_Deconstruct.htm)|
Метод, выполняющий деконструкцию структуры в набор переменных для
использования в C#.  
---|---  
[Deserialize(BinaryReader)](M_Tessa_Platform_Operations_OperationStateAndProgress_Deserialize_1.htm)|
Десериализует объект из бинарной формы.  
[Deserialize(Dictionary<String,
Object>)](M_Tessa_Platform_Operations_OperationStateAndProgress_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
[Equals](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\))| Indicates whether this instance and a
specified object are equal.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode)| Returns the hash code for this instance.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Serialize(BinaryWriter)](M_Tessa_Platform_Operations_OperationStateAndProgress_Serialize_1.htm)|
Сериализует объект в бинарной форме.  
[Serialize(Dictionary<String,
Object>)](M_Tessa_Platform_Operations_OperationStateAndProgress_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
[ToString](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring)| Returns the fully qualified type name of this instance.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
##  __Методы расширения
[ConvertOperationStateAndProgressToStorage](M_Tessa_Web_Client_Helpers_CommonExtensions_ConvertOperationStateAndProgressToStorage.htm)|  
(Определяется
[CommonExtensions](T_Tessa_Web_Client_Helpers_CommonExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
