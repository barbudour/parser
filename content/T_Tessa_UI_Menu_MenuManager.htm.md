# MenuManager - класс
Объект, управляющий жизненным циклом меню.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class MenuManager
VB __Копировать
     Public NotInheritable Class MenuManager
C++ __Копировать
     public ref class MenuManager sealed
F# __Копировать
     [<SealedAttribute>]
    type MenuManager = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MenuManager
##  __Заметки
Объект должен быть недоступен для сборщика мусора, пока меню не будет закрыто,
поэтому рекомендуется размещать его в поле того объекта, который его создаёт.
## __Конструкторы
[MenuManager](M_Tessa_UI_Menu_MenuManager__ctor.htm)|  Создаёт экземпляр
класса с указанием его зависимостей.  
---|---  
## __Свойства
[Placement](P_Tessa_UI_Menu_MenuManager_Placement.htm)|  Расположение
контекстного меню относительно объекта, переданного в параметре метода
[ShowContextMenu(FrameworkElement)](M_Tessa_UI_Menu_MenuManager_ShowContextMenu.htm).
По умолчанию используется
[MousePoint](https://learn.microsoft.com/dotnet/api/system.windows.controls.primitives.placementmode).  
---|---  
[SetupItemCallback](P_Tessa_UI_Menu_MenuManager_SetupItemCallback.htm)|
Метод, выполняющий настройку добавляемых элементов, или null, если
дополнительной настройки не производится.  
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
[Initialize](M_Tessa_UI_Menu_MenuManager_Initialize.htm)|  Инициализирует меню
и отслеживает его закрытие, если оно контекстное.  
[IsEmpty](M_Tessa_UI_Menu_MenuManager_IsEmpty.htm)|  Возвращает признак того,
что в меню отсутствуют отображаемые пользователю пункты меню. Такое меню не
будет выводиться методом
[ShowContextMenu(FrameworkElement)](M_Tessa_UI_Menu_MenuManager_ShowContextMenu.htm).  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Refresh](M_Tessa_UI_Menu_MenuManager_Refresh.htm)|  Заполняет меню,
предварительно удаляя его содержимое.  
[ShowContextMenu](M_Tessa_UI_Menu_MenuManager_ShowContextMenu.htm)|
Отображает контекстное меню, если оно не пустое, и возвращает созданное меню,
что если оно было отображено, или null, если не было создано ни одного
элемента, видимого пользователю, или меню не является контекстным.  
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
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
