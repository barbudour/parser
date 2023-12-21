# KrProcessUIContainer - класс
Объект, содержащий информацию о UI обработчиках этапов подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrProcessUIContainer : IKrProcessUIContainer
VB __Копировать
     Public NotInheritable Class KrProcessUIContainer
    	Implements IKrProcessUIContainer
C++ __Копировать
     public ref class KrProcessUIContainer sealed : IKrProcessUIContainer
F# __Копировать
     [<SealedAttribute>]
    type KrProcessUIContainer = 
        class
            interface IKrProcessUIContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessUIContainer
Implements
    [IKrProcessUIContainer](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrProcessUIContainer.htm)
##  __Конструкторы
[KrProcessUIContainer](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrProcessUIContainer__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
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
[RegisterUIHandler(Type)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrProcessUIContainer_RegisterUIHandler.htm)|
Регистрирует UI обработчик этапа для любого типа этапа.  
[RegisterUIHandler(StageTypeDescriptor,
Type)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrProcessUIContainer_RegisterUIHandler_1.htm)|
Регистрирует UI обработчик этапа для типа этапа с заданным дескриптором.  
[RegisterUIHandler<T>()](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrProcessUIContainer_RegisterUIHandler__1.htm)|
Регистрирует UI обработчик этапа для любого типа этапа.  
[RegisterUIHandler<T>(StageTypeDescriptor)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrProcessUIContainer_RegisterUIHandler__1_1.htm)|
Регистрирует UI обработчик этапа для типа этапа с заданным дескриптором.  
[ResolveUIHandlers](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrProcessUIContainer_ResolveUIHandlers.htm)|
Возвращает список зарегистрированных UI обработчиков для типа этапа с
указанным идентификатором и обработчиков, выполняющихся для любого типа этапа.  
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
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers - пространство
имён](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)
