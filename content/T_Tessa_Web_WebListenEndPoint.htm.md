# WebListenEndPoint - класс
Информация по точке прослушивания для Kestrel.
## __Definition
 **Пространство имён:** [Tessa.Web](N_Tessa_Web.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WebListenEndPoint
VB __Копировать
     Public NotInheritable Class WebListenEndPoint
C++ __Копировать
     public ref class WebListenEndPoint sealed
F# __Копировать
     [<SealedAttribute>]
    type WebListenEndPoint = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebListenEndPoint
##  __Свойства
[IPEndPoint](P_Tessa_Web_WebListenEndPoint_IPEndPoint.htm)|  Информация по
конечной точке с IP-адресом и портом, прослушивание которой выполняется, или
null, если прослушивание выполняется не для конкретного IP-адреса. Значение
указано в том случае, если
[ListenMode](P_Tessa_Web_WebListenEndPoint_ListenMode.htm) равен
[IPEndpoint](T_Tessa_Web_WebListenMode.htm).  
---|---  
[ListenMode](P_Tessa_Web_WebListenEndPoint_ListenMode.htm)|  Способ
прослушивания конечных точек (endpoints) в Kestrel.  
[Port](P_Tessa_Web_WebListenEndPoint_Port.htm)|  Номер порта, для которого
выполняется прослушивание.  
[Protocol](P_Tessa_Web_WebListenEndPoint_Protocol.htm)|  Протокол, для
которого выполняется прослушивание. Рекомендуется указать
[HttpProtocol](F_Tessa_Web_WebHelper_HttpProtocol.htm) или
[HttpsProtocol](F_Tessa_Web_WebHelper_HttpsProtocol.htm).  
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
[ListenAnyAddress](M_Tessa_Web_WebListenEndPoint_ListenAnyAddress.htm)|
Создаёт объект, содержащий информацию по прослушиванию по всем IP-адресам,
используя интерфейсы IPv6 [::] или IPv4 0.0.0.0, если IPv6 недоступен.  
[ListenIPEndPoint](M_Tessa_Web_WebListenEndPoint_ListenIPEndPoint.htm)|
Создаёт объект, содержащий информацию по прослушиванию заданной конечной точки
с IP-адресом и портом.  
[ListenLocalhost](M_Tessa_Web_WebListenEndPoint_ListenLocalhost.htm)|  Создаёт
объект, содержащий информацию по прослушиванию localhost (loopback-интерфейс)
для IPv4 и IPv6.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Web_WebListenEndPoint_ToString.htm)|  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Web - пространство имён](N_Tessa_Web.htm)
