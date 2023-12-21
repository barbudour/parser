# ConfigurationDataProvider - класс
Объект, описывающий поставщик данных для строки подключения.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ConfigurationDataProvider
VB __Копировать
     Public NotInheritable Class ConfigurationDataProvider
C++ __Копировать
     public ref class ConfigurationDataProvider sealed
F# __Копировать
     [<SealedAttribute>]
    type ConfigurationDataProvider = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConfigurationDataProvider
##  __Конструкторы
[ConfigurationDataProvider](M_Tessa_Platform_ConfigurationDataProvider__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Default](P_Tessa_Platform_ConfigurationDataProvider_Default.htm)|  Поставщик
данных по умолчанию.  
---|---  
[Name](P_Tessa_Platform_ConfigurationDataProvider_Name.htm)|  Имя поставщика
данных.  
[TypeName](P_Tessa_Platform_ConfigurationDataProvider_TypeName.htm)|  Имя типа
данных. Может быть равно null или пустой строке, если используется имя типа по
умолчанию.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDataProvider](M_Tessa_Platform_ConfigurationDataProvider_GetDataProvider.htm)|
Возвращает объект IDataProvider для заданного типа
[TypeName](P_Tessa_Platform_ConfigurationDataProvider_TypeName.htm).
Возвращённое значение не равно null.  
[GetDbProviderFactory()](M_Tessa_Platform_ConfigurationDataProvider_GetDbProviderFactory.htm)|
Возвращает объект
[DbProviderFactory](https://learn.microsoft.com/dotnet/api/system.data.common.dbproviderfactory)
для заданного типа
[TypeName](P_Tessa_Platform_ConfigurationDataProvider_TypeName.htm).
Возвращённое значение не равно null.  
[GetDbProviderFactory(String)](M_Tessa_Platform_ConfigurationDataProvider_GetDbProviderFactory_1.htm)|
Возвращает объект
[DbProviderFactory](https://learn.microsoft.com/dotnet/api/system.data.common.dbproviderfactory)
для заданного типа
[TypeName](P_Tessa_Platform_ConfigurationDataProvider_TypeName.htm).
Возвращённое значение не равно null.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
