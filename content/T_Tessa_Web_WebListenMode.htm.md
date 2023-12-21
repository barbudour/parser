# WebListenMode - перечисление
Способ прослушивания конечных точек (endpoints) в Kestrel.
## __Definition
 **Пространство имён:** [Tessa.Web](N_Tessa_Web.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public enum WebListenMode
VB __Копировать
     Public Enumeration WebListenMode
C++ __Копировать
     public enum class WebListenMode
F# __Копировать
     type WebListenMode
##  __Члены
IPEndpoint| 0|  Прослушивание выполняется на конечной точке по указанному IP-
адресу и порту.  
---|---|---  
Localhost| 1|  Прослушивание выполняется для localhost (loopback-интерфейс)
для IPv4 и IPv6.  
AnyAddress| 2|  Прослушивание выполняется по всем IP-адресам, используя
интерфейсы IPv6 [::] или IPv4 0.0.0.0, если IPv6 недоступен.  
## __См. также
#### Ссылки
[Tessa.Web - пространство имён](N_Tessa_Web.htm)
