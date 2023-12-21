# SettingsProvider - класс
Объект, предоставляющий доступ к объекту с настройками из любого потока. К
объекту возможно безопасное обращение из нескольких потоков.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SettingsProvider : ISettingsProvider, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class SettingsProvider
    	Implements ISettingsProvider, IDisposable
C++ __Копировать
     public ref class SettingsProvider sealed : ISettingsProvider, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type SettingsProvider = 
        class
            interface ISettingsProvider
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SettingsProvider
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ISettingsProvider](T_Tessa_Platform_Settings_ISettingsProvider.htm)
##  __Конструкторы
[SettingsProvider](M_Tessa_Platform_Settings_SettingsProvider__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[Dispose](M_Tessa_Platform_Settings_SettingsProvider_Dispose.htm)| Освобождает
ресурсы, занимаемые объектом.  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSettingsAsync](M_Tessa_Platform_Settings_SettingsProvider_GetSettingsAsync.htm)|
Возвращает настройки расширений. Возвращаемое значение не равно null. При
первом обращении выполняет инициализацию настроек. Если при инициализации
возникли ошибки, то выбрасывается исключение.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync](M_Tessa_Platform_Settings_SettingsProvider_InvalidateAsync.htm)|
Удаляет закэшированные настройки так, что при следующем обращении к настройкам
будет выполнена их инициализация.  
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
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
