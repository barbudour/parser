# ThemePropertyInfo - класс
Описание свойства темы.
## __Definition
 **Пространство имён:** [Tessa.Themes](N_Tessa_Themes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ThemePropertyInfo : StorageSerializable, 
    	IThemePropertyInfo, ISealable
VB __Копировать
     Public NotInheritable Class ThemePropertyInfo
    	Inherits StorageSerializable
    	Implements IThemePropertyInfo, ISealable
C++ __Копировать
     public ref class ThemePropertyInfo sealed : public StorageSerializable, 
    	IThemePropertyInfo, ISealable
F# __Копировать
     [<SealedAttribute>]
    type ThemePropertyInfo = 
        class
            inherit StorageSerializable
            interface IThemePropertyInfo
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ ThemePropertyInfo
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IThemePropertyInfo](T_Tessa_Themes_IThemePropertyInfo.htm)
##  __Конструкторы
[ThemePropertyInfo(IThemePropertyInfo)](M_Tessa_Themes_ThemePropertyInfo__ctor.htm)|
Создаёт экземпляр класса, копируя свойства из заданного объекта.  
---|---  
[ThemePropertyInfo(ThemePropertyType)](M_Tessa_Themes_ThemePropertyInfo__ctor_1.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
## __Свойства
[IsSealed](P_Tessa_Themes_ThemePropertyInfo_IsSealed.htm)| Признак того, что
объект был защищён от изменений.  
---|---  
[PropertyType](P_Tessa_Themes_ThemePropertyInfo_PropertyType.htm)|  Тип
свойства темы.  
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
[DeserializeCore](M_Tessa_Themes_ThemePropertyInfo_DeserializeCore.htm)|
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Themes_ThemePropertyInfo_Seal.htm)| Защищает объект от
изменений.  
[Serialize](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Themes_ThemePropertyInfo_SerializeCore.htm)| Выполняет
сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryParse](M_Tessa_Themes_ThemePropertyInfo_TryParse.htm)|  Возвращает объект
с указанным [ThemePropertyType](T_Tessa_Themes_ThemePropertyType.htm) по
значению в строке или null, если значение не удалось получить.  
## __Поля
[PropertyTypeKey](F_Tessa_Themes_ThemePropertyInfo_PropertyTypeKey.htm)|  Ключ
для хранения свойства
[PropertyType](P_Tessa_Themes_ThemePropertyInfo_PropertyType.htm) в
сериализованном виде.  
---|---  
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
[Tessa.Themes - пространство имён](N_Tessa_Themes.htm)
