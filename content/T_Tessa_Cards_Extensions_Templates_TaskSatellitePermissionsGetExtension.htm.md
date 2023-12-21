# TaskSatellitePermissionsGetExtension - класс
Шаблон расширения на загрузку разрешений Permissions для карточки-сателлита
для задачи.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class TaskSatellitePermissionsGetExtension : CardGetExtension
VB __Копировать
     Public MustInherit Class TaskSatellitePermissionsGetExtension
    	Inherits CardGetExtension
C++ __Копировать
     public ref class TaskSatellitePermissionsGetExtension abstract : public CardGetExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type TaskSatellitePermissionsGetExtension = 
        class
            inherit CardGetExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm) __ TaskSatellitePermissionsGetExtension
##  __Конструкторы
[TaskSatellitePermissionsGetExtension](M_Tessa_Cards_Extensions_Templates_TaskSatellitePermissionsGetExtension__ctor.htm)|
Инициализирует новый экземпляр класса TaskSatellitePermissionsGetExtension  
---|---  
##  __Свойства
[FileIsExternalKey](P_Tessa_Cards_Extensions_Templates_TaskSatellitePermissionsGetExtension_FileIsExternalKey.htm)|
Имя уникального ключа, по которому в информации по файлу сателлита file.Info
будет указан признак того, что файл виртуальный и на самом деле относится к
основной карточке. Если в файле ключ не указан, то файл относится именно к
сателлиту, т.е. это невиртуальный файл.  
---|---  
## __Методы
[AfterRequest](M_Tessa_Cards_Extensions_Templates_TaskSatellitePermissionsGetExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
(Переопределяет
[CardGetExtension.AfterRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
[CanModifyTaskCardAsync](M_Tessa_Cards_Extensions_Templates_TaskSatellitePermissionsGetExtension_CanModifyTaskCardAsync.htm)|
Возвращает признак того, что карточку-сателлит разрешено сохранять на
основании данных по заданию.  
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
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
