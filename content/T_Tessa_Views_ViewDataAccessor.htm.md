# ViewDataAccessor - класс
DataAccesor предоставляющий методы манипуляции моделями представлений
сохраненым в базе данных
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ViewDataAccessor
VB __Копировать
     Public NotInheritable Class ViewDataAccessor
C++ __Копировать
     public ref class ViewDataAccessor sealed
F# __Копировать
     [<SealedAttribute>]
    type ViewDataAccessor = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewDataAccessor
##  __Конструкторы
[ViewDataAccessor](M_Tessa_Views_ViewDataAccessor__ctor.htm)|  Инициализирует
новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Методы
[AddViewAsync](M_Tessa_Views_ViewDataAccessor_AddViewAsync.htm)|  Осуществляет
добавление представления в БД. Со стороны БД должен осуществляться контроль
уникальности [имен представлений](P_Tessa_Views_TessaViewModel_Alias.htm)  
---|---  
[ChangeViewAsync](M_Tessa_Views_ViewDataAccessor_ChangeViewAsync.htm)|
Осуществляет обновление информации о представлении  
[ClearAsync](M_Tessa_Views_ViewDataAccessor_ClearAsync.htm)|  Осуществляет
очистку справочника представлений  
[DeleteViewAsync](M_Tessa_Views_ViewDataAccessor_DeleteViewAsync.htm)|
Удаляет представление с идентификатором RowID  
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
[GetAccessibleUserViewsAsync](M_Tessa_Views_ViewDataAccessor_GetAccessibleUserViewsAsync.htm)|
Получает из базы данных список алиасов представлений доступных пользователю  
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
[GetUserRolesAsync](M_Tessa_Views_ViewDataAccessor_GetUserRolesAsync.htm)|
Получает из базы данных список идентификаторов ролей в которых состоит
пользователь  
[GetViewAsync](M_Tessa_Views_ViewDataAccessor_GetViewAsync.htm)|  Возвращает
представление по идентификатору  
[GetViewByAliasAsync](M_Tessa_Views_ViewDataAccessor_GetViewByAliasAsync.htm)|
Возвращает модель представления по алиасу  
[GetViewsAsync](M_Tessa_Views_ViewDataAccessor_GetViewsAsync.htm)|  Возвращает
список представлений  
[ImportViewsAsync](M_Tessa_Views_ViewDataAccessor_ImportViewsAsync.htm)|
Осуществляет импорт представлений по алису представления.  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
