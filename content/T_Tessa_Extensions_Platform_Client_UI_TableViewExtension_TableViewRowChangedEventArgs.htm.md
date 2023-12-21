# TableViewRowChangedEventArgs - класс
Аргументы изменения строки таблицы-предствления
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TableViewRowChangedEventArgs : EventArgs
VB __Копировать
     Public NotInheritable Class TableViewRowChangedEventArgs
    	Inherits EventArgs
C++ __Копировать
     public ref class TableViewRowChangedEventArgs sealed : public EventArgs
F# __Копировать
     [<SealedAttribute>]
    type TableViewRowChangedEventArgs = 
        class
            inherit EventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __ TableViewRowChangedEventArgs
##  __Конструкторы
[TableViewRowChangedEventArgs](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs__ctor.htm)|
Инициализирует новый экземпляр класса TableViewRowChangedEventArgs  
---|---  
##  __Свойства
[CardRow](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs_CardRow.htm)|
Строка основной секции. Всегда задана.  
---|---  
[ChangedFieldName](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs_ChangedFieldName.htm)|
Имя измененного в строке поля. Может быть null  
[ChangeType](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs_ChangeType.htm)|
Тип изменения  
[OwnedCardRow](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs_OwnedCardRow.htm)|
Измененная (так же добавленная или удаленная) строка дочерней секции. Может
быть null.  
[OwnedSectionName](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs_OwnedSectionName.htm)|
Имя дочерней секции, в которой изменилась строка. Может быть null  
[Row](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs_Row.htm)|
Строка представления, на которую могут повлиять изменения  
[RowID](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs_RowID.htm)|
RowID строки основной секции  
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
