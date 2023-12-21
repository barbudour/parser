# LinkContext - класс
Контекст обработчика по открытию ссылок.
## __Definition
 **Пространство имён:** [Tessa.Platform.Links](N_Tessa_Platform_Links.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LinkContext : ILinkContext
VB __Копировать
     Public NotInheritable Class LinkContext
    	Implements ILinkContext
C++ __Копировать
     public ref class LinkContext sealed : ILinkContext
F# __Копировать
     [<SealedAttribute>]
    type LinkContext = 
        class
            interface ILinkContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LinkContext
Implements
    [ILinkContext](T_Tessa_Platform_Links_ILinkContext.htm)
##  __Конструкторы
[LinkContext](M_Tessa_Platform_Links_LinkContext__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Action](P_Tessa_Platform_Links_LinkContext_Action.htm)| Действие, указанное в
ссылке. Действие определяет, какой обработчик ссылки будет вызван.  
---|---  
[CancellationToken](P_Tessa_Platform_Links_LinkContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[Container](P_Tessa_Platform_Links_LinkContext_Container.htm)|  Контейнер
Unity, из которого обработчик ссылки может получить сервисы и другие
зависимости.  
[Handled](P_Tessa_Platform_Links_LinkContext_Handled.htm)|  Признак того, что
ссылка была обработана обработчиком. Если значение установлено равным true, то
окно приложения будет активировано при завершении обработки ссылки.  
[Parameters](P_Tessa_Platform_Links_LinkContext_Parameters.htm)|  Хеш-таблица
с параметрами ссылки, ключом которой является название параметра, а значением
- строковая интерпретация значения параметра, заданная в ссылке.  
[Session](P_Tessa_Platform_Links_LinkContext_Session.htm)| Текущая сессия.  
##  __Методы
[ActivateShellAsync](M_Tessa_Platform_Links_LinkContext_ActivateShellAsync.htm)|
Активирует основное окно приложения. Если окно было свёрнуто, то оно
разворачивается.  
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
[GetParameters](M_Tessa_Platform_Links_LinkContext_GetParameters.htm)|
Возвращает параметры ссылки по его тексту. Возвращаемое значение не равно
null. Параметры могут использоваться в методе [TryParse(Dictionary<String,
String>, ISession, IUnityContainer, Func<CancellationToken, Task>,
CancellationToken)](M_Tessa_Platform_Links_LinkContext_TryParse.htm).  
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
[TryParse(Dictionary<String, String>, ISession, IUnityContainer,
Func<CancellationToken, Task>,
CancellationToken)](M_Tessa_Platform_Links_LinkContext_TryParse.htm)|
Выполняет парсинг ссылки Tessa и возвращает контекст с информацией по ссылке
или null, если парсинг сообщения не удался или сообщение не содержит ссылок.  
[TryParse(String, ISession, IUnityContainer, Func<CancellationToken, Task>,
CancellationToken)](M_Tessa_Platform_Links_LinkContext_TryParse_1.htm)|
Выполняет разбор текста linkText, содержащего ссылку, и возвращает контекст с
информацией по ссылке или null, если парсинг сообщения не удался или сообщение
не содержит ссылок.  
## __Методы расширения
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
[Tessa.Platform.Links - пространство имён](N_Tessa_Platform_Links.htm)
