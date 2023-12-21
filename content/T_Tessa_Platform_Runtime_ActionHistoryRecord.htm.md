# ActionHistoryRecord - класс
Запись в истории действий карточки. Объект не сериализуется стандартными
средствами.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ActionHistoryRecord
VB __Копировать
     Public NotInheritable Class ActionHistoryRecord
C++ __Копировать
     public ref class ActionHistoryRecord sealed
F# __Копировать
     [<SealedAttribute>]
    type ActionHistoryRecord = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ActionHistoryRecord
##  __Конструкторы
[ActionHistoryRecord](M_Tessa_Platform_Runtime_ActionHistoryRecord__ctor.htm)|
Создаёт экземпляр класса с указанием всех его свойств.  
---|---  
## __Свойства
[Action](P_Tessa_Platform_Runtime_ActionHistoryRecord_Action.htm)|  Тип
действия.  
---|---  
[Digest](P_Tessa_Platform_Runtime_ActionHistoryRecord_Digest.htm)|  Краткое
описание карточки или действия с карточкой.  
[ID](P_Tessa_Platform_Runtime_ActionHistoryRecord_ID.htm)|  Идентификатор
карточки.  
[Modified](P_Tessa_Platform_Runtime_ActionHistoryRecord_Modified.htm)|  Дата и
время действия с карточкой.  
[ModifiedByID](P_Tessa_Platform_Runtime_ActionHistoryRecord_ModifiedByID.htm)|
Идентификатор пользователя, который произвёл действие с карточкой.  
[ModifiedByName](P_Tessa_Platform_Runtime_ActionHistoryRecord_ModifiedByName.htm)|
Имя пользователя, который произвёл действие с карточкой.  
[Request](P_Tessa_Platform_Runtime_ActionHistoryRecord_Request.htm)|  Запрос
на действие с карточкой.  
[RequestJson](P_Tessa_Platform_Runtime_ActionHistoryRecord_RequestJson.htm)|
Сериализованный запрос на действие с карточкой.  
[RowID](P_Tessa_Platform_Runtime_ActionHistoryRecord_RowID.htm)|
Идентификатор записи об истории карточки.  
[SessionID](P_Tessa_Platform_Runtime_ActionHistoryRecord_SessionID.htm)|
Сессия, в рамках которой выполнялось действие, или null, если действие было
выполнено вне пределов сессии или в старых сборках платформы, не
поддерживавших сессию в истории действий.  
[TypeCaption](P_Tessa_Platform_Runtime_ActionHistoryRecord_TypeCaption.htm)|
Отображаемое имя типа карточки.  
[TypeID](P_Tessa_Platform_Runtime_ActionHistoryRecord_TypeID.htm)|
Идентификатор типа карточки.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
