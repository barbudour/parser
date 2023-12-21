# Tessa.Platform.GuidComb - пространство имён
API для генерации Guid, которые сортируются в порядке генерации.
##  __Классы
[BaseGuidCombProvider](T_Tessa_Platform_GuidComb_BaseGuidCombProvider.htm)|  
---|---  
[GuidCombProviders](T_Tessa_Platform_GuidComb_GuidCombProviders.htm)|  
[PostgreSqlGuidCombProvider](T_Tessa_Platform_GuidComb_PostgreSqlGuidCombProvider.htm)|  
[SqlGuidCombProvider](T_Tessa_Platform_GuidComb_SqlGuidCombProvider.htm)|  
[UnixDateTimeStrategy](T_Tessa_Platform_GuidComb_UnixDateTimeStrategy.htm)|
This strategy stores the Unix epoch timestamp, scaled to milliseconds, in 48
unsigned bits. The allowed date range is 1970-01-01 to 8419-05-26.  
[UtcNoRepeatTimestampProvider](T_Tessa_Platform_GuidComb_UtcNoRepeatTimestampProvider.htm)|  
## __Интерфейсы
[IGuidCombDateTimeStrategy](T_Tessa_Platform_GuidComb_IGuidCombDateTimeStrategy.htm)|
Represents a mechanism for converting DateTime values back and forth to byte
arrays. Strategies can differ depending on how many bytes of the GUID you wish
to overwrite, what time resolution you want, etc.  
---|---  
[IGuidCombProvider](T_Tessa_Platform_GuidComb_IGuidCombProvider.htm)|  An
interface for working with COMB GUIDs, implemented for both variants.  
## __Делегаты
[GuidProvider](T_Tessa_Platform_GuidComb_GuidProvider.htm)|  
---|---  
[TimestampProvider](T_Tessa_Platform_GuidComb_TimestampProvider.htm)|
