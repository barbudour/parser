# TableViewRowAddingEventArgs - класс
Аргументы события, происходящего перед добавлением строки в таблице
[CardTableViewControlViewModel](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class TableViewRowAddingEventArgs : RowAddingEventArgs
VB __Копировать
     Public Class TableViewRowAddingEventArgs
    	Inherits RowAddingEventArgs
C++ __Копировать
     public ref class TableViewRowAddingEventArgs : public RowAddingEventArgs
F# __Копировать
     type TableViewRowAddingEventArgs = 
        class
            inherit RowAddingEventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __[DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm) __[RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm) __ TableViewRowAddingEventArgs
##  __Конструкторы
[TableViewRowAddingEventArgs](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowAddingEventArgs__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Cancel](P_Tessa_UI_Cards_Controls_RowAddingEventArgs_Cancel.htm)|  Признак
того, что добавление строки отменяется.  
(Унаследован от
[RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm))  
---|---  
[CancellationToken](P_Tessa_UI_Cards_Controls_RowAddingEventArgs_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm))  
[CardModel](P_Tessa_UI_Cards_Controls_RowAddingEventArgs_CardModel.htm)|
Модель карточки, в которой расположена строка
[Row](P_Tessa_UI_Cards_Controls_RowAddingEventArgs_Row.htm).  
(Унаследован от
[RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm))  
[Control](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowAddingEventArgs_Control.htm)|
Контрол, в рамках которого выполняется событие.  
[Row](P_Tessa_UI_Cards_Controls_RowAddingEventArgs_Row.htm)|  Строка карточки,
с которой производится действие.  
(Унаследован от
[RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm))  
[RowIndex](P_Tessa_UI_Cards_Controls_RowAddingEventArgs_RowIndex.htm)|  Индекс
вставляемого элемента, по умолчанию Rows.Count.  
(Унаследован от
[RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm))  
[Rows](P_Tessa_UI_Cards_Controls_RowAddingEventArgs_Rows.htm)|  Список всех
строк в таблице.  
(Унаследован от
[RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm))  
##  __Методы
[Defer](M_Tessa_Platform_DeferredEventArgs_Defer.htm)|  Возвращает объект,
обеспечивающий ожидание действия. Вызовите метод в блоке using, внутри
которого выполняйте любые ожидания await.  
(Унаследован от [DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm))  
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
