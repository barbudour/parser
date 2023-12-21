# IPrintDialogProvider - интерфейс
Объект, управляющий отображением диалога печати для страницы со штрих-кодом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.DocLoad](N_Tessa_Extensions_Default_Client_DocLoad.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPrintDialogProvider
VB __Копировать
     Public Interface IPrintDialogProvider
C++ __Копировать
     public interface class IPrintDialogProvider
F# __Копировать
     type IPrintDialogProvider = interface end
##  __Методы
[IsPrinterSelectionEnabled](M_Tessa_Extensions_Default_Client_DocLoad_IPrintDialogProvider_IsPrinterSelectionEnabled.htm)|
Отображать ли кнопку выбора принтера  
---|---  
[PrintDocumentAsync](M_Tessa_Extensions_Default_Client_DocLoad_IPrintDialogProvider_PrintDocumentAsync.htm)|
Выполняет печать указанного документа с параметрами печати, которые ранее были
выбраны в диалоге [SelectPrinterDialogAsync(Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Client_DocLoad_IPrintDialogProvider_SelectPrinterDialogAsync.htm).  
[SelectPrinterDialogAsync](M_Tessa_Extensions_Default_Client_DocLoad_IPrintDialogProvider_SelectPrinterDialogAsync.htm)|
Отображает диалог для печати. Возвращает признак того, что пользователь
подтвердил печать.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.DocLoad - пространство
имён](N_Tessa_Extensions_Default_Client_DocLoad.htm)
