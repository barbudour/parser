# FreeBusyViewType - перечисление
Defines the type of free/busy information returned by a GetUserAvailability
operation.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum FreeBusyViewType
VB __Копировать
     Public Enumeration FreeBusyViewType
C++ __Копировать
     public enum class FreeBusyViewType
F# __Копировать
     type FreeBusyViewType
##  __Члены
None| 0|  No view could be returned. This value cannot be specified in a call
to GetUserAvailability.  
---|---|---  
MergedOnly| 1|  Represents an aggregated free/busy stream. In cross-forest
scenarios in which the target user in one forest does not have an Availability
service configured, the Availability service of the requestor retrieves the
target user's free/busy information from the free/busy public folder. Because
public folders only store free/busy information in merged form, MergedOnly is
the only available information.  
FreeBusy| 2|  Represents the legacy status information: free, busy, tentative,
and OOF. This also includes the start/end times of the appointments. This view
is richer than the legacy free/busy view because individual meeting start and
end times are provided instead of an aggregated free/busy stream.  
FreeBusyMerged| 3|  Represents all the properties in FreeBusy with a stream of
merged free/busy availability information.  
Detailed| 4|  Represents the legacy status information: free, busy, tentative,
and OOF; the start/end times of the appointments; and various properties of
the appointment such as subject, location, and importance. This requested view
will return the maximum amount of information for which the requesting user is
privileged. If merged free/busy information only is available, as with
requesting information for users in a Microsoft Exchange Server 2003 forest,
MergedOnly will be returned. Otherwise, FreeBusy or Detailed will be returned.  
DetailedMerged| 5|  Represents all the properties in Detailed with a stream of
merged free/busy availability information. If only merged free/busy
information is available, for example if the mailbox exists on a computer
running Exchange 2003, MergedOnly will be returned. Otherwise, FreeBusyMerged
or DetailedMerged will be returned.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
