# CardServerPermissionsProvider - класс
Объект, не предоставляющий прав доступа, но реализующий все методы интерфейса
[ICardServerPermissionsProvider](T_Tessa_Cards_ICardServerPermissionsProvider.htm).
Зарегистрирован по умолчанию, если расширения типового решения отсутствуют.
Наследники объекта могут переопределять методы и добавлять поведения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardServerPermissionsProvider : ICardServerPermissionsProvider
VB __Копировать
     Public Class CardServerPermissionsProvider
    	Implements ICardServerPermissionsProvider
C++ __Копировать
     public ref class CardServerPermissionsProvider : ICardServerPermissionsProvider
F# __Копировать
     type CardServerPermissionsProvider = 
        class
            interface ICardServerPermissionsProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardServerPermissionsProvider
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrCardServerPermissionsProvider](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrCardServerPermissionsProvider.htm)
Implements
    [ICardServerPermissionsProvider](T_Tessa_Cards_ICardServerPermissionsProvider.htm)
##  __Конструкторы
[CardServerPermissionsProvider](M_Tessa_Cards_CardServerPermissionsProvider__ctor.htm)|
Инициализирует новый экземпляр класса CardServerPermissionsProvider  
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
[SetFullPermissions(CardDeleteRequest)](M_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
удаление карточки.  
[SetFullPermissions(CardGetFileContentRequest)](M_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions_1.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку содержимого файла.  
[SetFullPermissions(CardGetFileVersionsRequest)](M_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions_2.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку версий файла.  
[SetFullPermissions(CardGetRequest)](M_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions_3.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку карточки.  
[SetFullPermissions(CardNewRequest)](M_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions_4.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
создание карточки.  
[SetFullPermissions(CardStoreRequest)](M_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions_5.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
сохранение карточки.  
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
