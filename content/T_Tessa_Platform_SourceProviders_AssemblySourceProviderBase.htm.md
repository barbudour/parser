# AssemblySourceProviderBase - класс
Базовый класс для SourceProvider'ов реализующих доступ к контенту из сборки
приложения (assembly).
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class AssemblySourceProviderBase : SourceProviderBase
VB __Копировать
     Public MustInherit Class AssemblySourceProviderBase
    	Inherits SourceProviderBase
C++ __Копировать
     public ref class AssemblySourceProviderBase abstract : public SourceProviderBase
F# __Копировать
     [<AbstractClassAttribute>]
    type AssemblySourceProviderBase = 
        class
            inherit SourceProviderBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm) __ AssemblySourceProviderBase
Derived
[Tessa.Platform.SourceProviders.AssemblySourceContentProvider](T_Tessa_Platform_SourceProviders_AssemblySourceContentProvider.htm)
[Tessa.Platform.SourceProviders.AssemblySourceDirectoryProvider](T_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider.htm)
##  __Конструкторы
[AssemblySourceProviderBase](M_Tessa_Platform_SourceProviders_AssemblySourceProviderBase__ctor.htm)|
Инициализирует новый экземпляр класса AssemblySourceProviderBase.  
---|---  
## __Свойства
[Assembly](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_Assembly.htm)|
Сборка, содержащая ресурсы.  
---|---  
[DirectoryPath](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_DirectoryPath.htm)|
Путь до ресурса относительно сборки.  
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm)|
Флаг указывает на то, что источник предназначен только для чтения. Зависит от
реализаций провайдеров.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
##  __Методы
[CheckReadOnly](M_Tessa_Platform_SourceProviders_SourceProviderBase_CheckReadOnly.htm)|
Проверяет, является ли объект доступен только для чтения
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm),
и выбрасывает исключение, если является.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
---|---  
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
[GetCachedNamesList](M_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_GetCachedNamesList.htm)|
Возвращает кэшированный список ресурсов расположенные в сборке по пути
[DirectoryPath](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_DirectoryPath.htm).  
[GetFullName](M_Tessa_Platform_SourceProviders_SourceProviderBase_GetFullName.htm)|  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetResourcePath](M_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_GetResourcePath.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsExistsAsync](M_Tessa_Platform_SourceProviders_SourceProviderBase_IsExistsAsync.htm)|  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
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
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)
