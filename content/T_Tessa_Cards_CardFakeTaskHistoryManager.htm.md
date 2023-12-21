# CardFakeTaskHistoryManager - класс
Объект, реализующий интерфейс
[ICardTaskHistoryManager](T_Tessa_Cards_ICardTaskHistoryManager.htm), но не
выполняющий действий. Все методы класса возвращают null. Объект доступен на
сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFakeTaskHistoryManager : ICardTaskHistoryManager
VB __Копировать
     Public NotInheritable Class CardFakeTaskHistoryManager
    	Implements ICardTaskHistoryManager
C++ __Копировать
     public ref class CardFakeTaskHistoryManager sealed : ICardTaskHistoryManager
F# __Копировать
     [<SealedAttribute>]
    type CardFakeTaskHistoryManager = 
        class
            interface ICardTaskHistoryManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardFakeTaskHistoryManager
Implements
    [ICardTaskHistoryManager](T_Tessa_Cards_ICardTaskHistoryManager.htm)
##  __Конструкторы
[CardFakeTaskHistoryManager](M_Tessa_Cards_CardFakeTaskHistoryManager__ctor.htm)|
Инициализирует новый экземпляр класса CardFakeTaskHistoryManager  
---|---  
##  __Свойства
[Instance](P_Tessa_Cards_CardFakeTaskHistoryManager_Instance.htm)| Экземпляр
класса.  
---|---  
##  __Методы
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
[GetGroupCaptionAsync](M_Tessa_Cards_CardFakeTaskHistoryManager_GetGroupCaptionAsync.htm)|
Возвращает название новой группы в истории заданий для заданных параметров.  
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
[ResolveGroupAsync](M_Tessa_Cards_CardFakeTaskHistoryManager_ResolveGroupAsync.htm)|
Возвращает группу в истории заданий, вычисленную для заданных параметров. При
необходимости группа будет создана. Также может быть создана родительская
группа, если указан её тип, но в карточке она отсутствует.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
