# NotificationHelper.GetCardLinkHtmlFooter - метод
Возвращает текст со ссылкой на карточку в desktop-клиенте или в web-клиенте в
формате html, который обычно добавляется снизу от основного содержимого
уведомления. Перед ссылкой может выводиться разделитель от выше расположенного
контента. Ссылка локализуется на текущий или заданный язык cultureInfo.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetCardLinkHtmlFooter(
    	string cardLink,
    	string webCardLink,
    	CultureInfo cultureInfo = null
    )
VB __Копировать
     Public Shared Function GetCardLinkHtmlFooter ( 
    	cardLink As String,
    	webCardLink As String,
    	Optional cultureInfo As CultureInfo = Nothing
    ) As String
C++ __Копировать
     public:
    static String^ GetCardLinkHtmlFooter(
    	String^ cardLink, 
    	String^ webCardLink, 
    	CultureInfo^ cultureInfo = nullptr
    )
F# __Копировать
     static member GetCardLinkHtmlFooter : 
            cardLink : string * 
            webCardLink : string * 
            ?cultureInfo : CultureInfo 
    (* Defaults:
            let _cultureInfo = defaultArg cultureInfo null
    *)
    -> string 
#### Параметры
cardLink [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ссылка на карточку, доступную в desktop-клиенте. Может быть равна null или пустой строке. 
webCardLink [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ссылка на карточку, доступную в web-клиенте. Может быть равен null или пустой строке. 
cultureInfo
[CultureInfo](https://learn.microsoft.com/dotnet/api/system.globalization.cultureinfo)
(Optional)
     Культура, используемая для локализации уведомлений, или null, если используется текущая культура. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Текст со ссылкой на карточку и разделителем, или пустую строку, если ссылка не
задана.
## __См. также
#### Ссылки
[NotificationHelper -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationHelper.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
