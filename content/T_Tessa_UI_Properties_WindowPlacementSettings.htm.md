# WindowPlacementSettings - класс
Информация по местоположению окна, которая сохраняется в конфигурации
[Settings](T_Tessa_UI_Properties_Settings.htm).
## __Definition
 **Пространство имён:** [Tessa.UI.Properties](N_Tessa_UI_Properties.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WindowPlacementSettings : StorageSerializable
VB __Копировать
     Public NotInheritable Class WindowPlacementSettings
    	Inherits StorageSerializable
C++ __Копировать
     public ref class WindowPlacementSettings sealed : public StorageSerializable
F# __Копировать
     [<SealedAttribute>]
    type WindowPlacementSettings = 
        class
            inherit StorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ WindowPlacementSettings
##  __Конструкторы
[WindowPlacementSettings](M_Tessa_UI_Properties_WindowPlacementSettings__ctor.htm)|
Инициализирует новый экземпляр класса WindowPlacementSettings  
---|---  
##  __Свойства
[Rect](P_Tessa_UI_Properties_WindowPlacementSettings_Rect.htm)|  
---|---  
[State](P_Tessa_UI_Properties_WindowPlacementSettings_State.htm)|  
[TypeName](P_Tessa_UI_Properties_WindowPlacementSettings_TypeName.htm)|  
## __Методы
[Deserialize](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
---|---  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_UI_Properties_WindowPlacementSettings_DeserializeCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsMatch(Window)](M_Tessa_UI_Properties_WindowPlacementSettings_IsMatch_1.htm)|  
[IsMatch(String,
Window)](M_Tessa_UI_Properties_WindowPlacementSettings_IsMatch.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Serialize](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_UI_Properties_WindowPlacementSettings_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[SetupFrom](M_Tessa_UI_Properties_WindowPlacementSettings_SetupFrom.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateTo](M_Tessa_UI_Properties_WindowPlacementSettings_UpdateTo.htm)|  
## __Поля
[HeightKey](F_Tessa_UI_Properties_WindowPlacementSettings_HeightKey.htm)|  
---|---  
[LeftKey](F_Tessa_UI_Properties_WindowPlacementSettings_LeftKey.htm)|  
[StateKey](F_Tessa_UI_Properties_WindowPlacementSettings_StateKey.htm)|  
[TopKey](F_Tessa_UI_Properties_WindowPlacementSettings_TopKey.htm)|  
[TypeKey](F_Tessa_UI_Properties_WindowPlacementSettings_TypeKey.htm)|  
[WidthKey](F_Tessa_UI_Properties_WindowPlacementSettings_WidthKey.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
##  __См. также
#### Ссылки
[Tessa.UI.Properties - пространство имён](N_Tessa_UI_Properties.htm)
