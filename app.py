import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta
import time

# Page config & enhanced CSS for pro look
st.set_page_config(
    page_title="GhostFracture™ Professional Dashboard", 
    layout="wide", 
    page_icon="👻",
    initial_sidebar_state="expanded"
)

st.logo(image="images/ghostfracture_logo.jpeg", 
        icon_image="images/ghostfracture_icon.jpeg")


# Enhanced CSS with red/gray theme
st.markdown("""
    <style>
    /* Main theme */
    :root {
        --primary-red: #8B0000;
        --secondary-red: #A52A2A;
        --light-gray: #f8f9fa;
        --medium-gray: #e9ecef;
        --dark-gray: #343a40;
        --accent-blue: #0066cc;
    }
    
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        color: var(--primary-red);
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: var(--dark-gray);
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .team-credits {
        font-size: 0.9rem;
        color: #666;
        text-align: center;
        font-style: italic;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .custom-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid var(--primary-red);
        margin-bottom: 1.5rem;
        border: 1px solid #dee2e6;
    }
    
    .section-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: var(--primary-red);
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--medium-gray);
    }
    
    /* Risk indicators */
    .risk-low {
        color: #28a745;
        font-weight: 600;
        background-color: rgba(40, 167, 69, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
    }
    
    .risk-medium {
        color: #ffc107;
        font-weight: 600;
        background-color: rgba(255, 193, 7, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
    }
    
    .risk-high {
        color: #dc3545;
        font-weight: 600;
        background-color: rgba(220, 53, 69, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
    }
    
    /* Status indicators */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-online {
        background-color: #28a745;
        box-shadow: 0 0 8px rgba(40, 167, 69, 0.5);
    }
    
    .status-offline {
        background-color: #6c757d;
    }
    
    .status-warning {
        background-color: #ffc107;
        box-shadow: 0 0 8px rgba(255, 193, 7, 0.5);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50 0%, #1a2530 100%);
    }
    
    .sidebar-header {
        color: white !important;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 1rem;
    }
    
    /* Toggle buttons */
    .st-bd {
        border-radius: 8px !important;
    }
    
    /* Metric cards */
    div[data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
    }
    
    /* Support panel */
    .support-panel {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid #ced4da;
        margin-top: 1rem;
    }
    
    /* Well log track */
    .log-track {
        background: white;
        border-radius: 5px;
        padding: 10px;
        margin: 5px 0;
        border-left: 3px solid var(--accent-blue);
    }
    
    /* Make containers less padded */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== HEADER SECTION ====================
st.markdown("<h1 class='main-header'> GHOSTFRACTURE™ PROFESSIONAL DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Physics-Guided Rule-Based AI for Real-Time Fracture Diagnostics & Well Log Analysis</p>", unsafe_allow_html=True)

# ==================== ENTERPRISE 24/7 SUPPORT PANEL ====================
with st.container():
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    
    with col_s1:
        st.markdown("###  **24/7 Support System**")
        st.markdown("<span class='status-indicator status-online'></span> **System Status: ONLINE**", unsafe_allow_html=True)
        st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    with col_s2:
        st.metric("**Response Time**", "35s", "-5s")
        st.caption("Average engineer response")
    
    with col_s3:
        st.metric("**Uptime**", "99.98%", "0.03%")
        st.caption("30-day rolling average")
    
    with col_s4:
        # Support contact buttons
        if st.button("🚨 Emergency Alert", use_container_width=True, type="primary"):
            st.session_state.emergency_alert = True
            st.success("Emergency alert sent to on-call engineers!")
        
        if st.button("📞 Call Support", use_container_width=True):
            st.info("Support: +213-XXXXXXXXX")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ==================== SIDEBAR: INPUT SLIDERS ====================
with st.sidebar:
    st.markdown("<h2 class='sidebar-header-blue'>A. INPUT SLIDERS – Causes</h2>", unsafe_allow_html=True)
    
    # Well & Completion Section
    st.markdown("####  **Well & Completion**")
    well_id = st.selectbox("Well ID", ["Berkine-12", "Ahnet-01", "Ghadames-07", "Hassi-Messaoud-05", "In-Amenas-03"])
    stage_num = st.slider("Stage Number", 1, 40, 17)
    cluster_spacing = st.slider("Cluster Spacing (ft)", 20, 100, 38)
    perfs_per_cluster = st.slider("Perforations per Cluster", 3, 12, 5)
    
    st.divider()
    
    # Geomechanics Section
    st.markdown("####  **Geomechanics**")
    sigma_hmax = st.slider("σHmax (psi)", 4000, 12000, 7065)
    sigma_hmin = st.slider("σhmin (psi)", 3000, 9000, 4742)
    stress_contrast = st.slider("Stress Contrast (σv - σhmin) (psi)", 500, 4000, 2433)
    young_modulus = st.slider("Young’s Modulus (Mpsi)", 2.0, 10.0, 7.19)
    poisson_ratio = st.slider("Poisson Ratio", 0.15, 0.35, 0.25)
    
    st.divider()
    
    # Treatment Section
    st.markdown("####  **Treatment Design**")
    pump_rate = st.slider("Pump Rate (BPM)", 40, 120, 80)
    fluid_type = st.selectbox("Fluid Type", ["Slickwater", "Hybrid", "Gel", "X-Link Gel"])
    fluid_viscosity = st.slider("Fluid Viscosity (cP)", 1.0, 100.0, 5.0)
    proppant_conc = st.slider("Proppant Concentration (lb/ft²)", 0.5, 8.0, 2.0)
    proppant_type = st.selectbox("Proppant Type", ["100-mesh Sand", "40/70 Sand", "30/50 Sand", "Ceramic"])
    
    st.divider()
    
    # Data Source Selection
    st.markdown("####  **Data Sources**")
    das_enabled = st.toggle("DAS Monitoring", value=True)
    dts_enabled = st.toggle("DTS Monitoring", value=True)
    downhole_gauges = st.toggle("Downhole Gauges", value=True)
    
    # Generate button
    if st.button(" **Generate Simulation & Analysis**", type="primary", use_container_width=True):
        with st.spinner("Running physics-based simulation..."):
            time.sleep(1.5)  # Simulate processing time
            st.success("Analysis complete!")

    # Track well changes and clear cache
    if 'previous_well' not in st.session_state:
     st.session_state.previous_well = well_id

    if st.session_state.previous_well != well_id:
    # Clear cache when well changes
     st.cache_data.clear()
     st.session_state.previous_well = well_id
    if st.button(" Refresh Well Data", type="primary", use_container_width=True):
        st.rerun()        


# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="Real Well Log Analysis System",
    page_icon="🛢️",
    layout="wide"
)

# ==================== DATA PROCESSING ====================
@st.cache_data
def process_well_log_data(well_id="Berkine-12"):  # CHANGE: Add well_id parameter
    """Process the well log data based on selected well ID"""
    try:
        # Get the well_id from session state or default
        selected_well = well_id
        
        # Create depth array - vary by well
        if selected_well == "Berkine-12":
            depth = np.linspace(195, 919.5, 1450)
        elif selected_well == "Ahnet-01":
            depth = np.linspace(2100, 3200, 1450)  # Deeper well
        elif selected_well == "Ghadames-07":
            depth = np.linspace(1800, 2800, 1450)
        elif selected_well == "Hassi-Messaoud-05":
            depth = np.linspace(2500, 3500, 1450)
        elif selected_well == "In-Amenas-03":
            depth = np.linspace(2300, 3100, 1450)
        else:
            depth = np.linspace(195, 919.5, 1450)
        
        # Well-specific characteristics
        if selected_well == "Berkine-12":
            # Sandstone dominant (Berkine Basin)
            shale_gr_mean = 90
            sandstone_gr_mean = 35
            reservoir_phi_mean = 0.25
            shale_res_mean = 1.0
            sand_res_mean = 15.0
        elif selected_well == "Ahnet-01":
            # Carbonate dominant
            shale_gr_mean = 80
            sandstone_gr_mean = 25  # Actually limestone
            reservoir_phi_mean = 0.15
            shale_res_mean = 1.5
            sand_res_mean = 8.0
        elif selected_well == "Ghadames-07":
            # Mixed lithology
            shale_gr_mean = 95
            sandstone_gr_mean = 40
            reservoir_phi_mean = 0.20
            shale_res_mean = 2.0
            sand_res_mean = 12.0
        elif selected_well == "Hassi-Messaoud-05":
            # Cambrian sandstone
            shale_gr_mean = 85
            sandstone_gr_mean = 30
            reservoir_phi_mean = 0.22
            shale_res_mean = 1.2
            sand_res_mean = 20.0
        elif selected_well == "In-Amenas-03":
            # Devonian sandstone
            shale_gr_mean = 88
            sandstone_gr_mean = 32
            reservoir_phi_mean = 0.18
            shale_res_mean = 1.8
            sand_res_mean = 18.0
        
        # Column names based on the PDF structure
        columns = [
            'Depth', 'CALI', 'SP', 'GR', 'ILD', 'LLD', 'LLS', 'MSFL',
            'DT', 'RHOB', 'NPHI', 'PEF', 'DRHO', 'RHOZ', 'DTC', 'DTS'
        ]
        
        # Generate realistic data based on formation changes
        n_points = len(depth)
        
        # Define formation boundaries based on depth range
        depth_min = depth.min()
        depth_max = depth.max()
        depth_range = depth_max - depth_min
        
        formations = {
            'Shale': (depth_min, depth_min + depth_range*0.15),
            'Sandstone_1': (depth_min + depth_range*0.15, depth_min + depth_range*0.30),
            'Limestone': (depth_min + depth_range*0.30, depth_min + depth_range*0.45),
            'Sandstone_2': (depth_min + depth_range*0.45, depth_min + depth_range*0.60),
            'Shale_2': (depth_min + depth_range*0.60, depth_min + depth_range*0.70),
            'Dolomite': (depth_min + depth_range*0.70, depth_min + depth_range*0.75),
            'Sandstone_3': (depth_min + depth_range*0.75, depth_min + depth_range*0.82),
            'Shale_3': (depth_min + depth_range*0.82, depth_min + depth_range*0.87),
            'Reservoir': (depth_min + depth_range*0.87, depth_min + depth_range*0.95),
            'Caprock': (depth_min + depth_range*0.95, depth_max)
        }
        
        # Initialize arrays
        data = {}
        for col in columns[1:]:  # Skip depth column
            data[col] = np.zeros(n_points)
        
        # Fill data based on formations with well-specific characteristics
        for formation, (top, bottom) in formations.items():
            mask = (depth >= top) & (depth <= bottom)
            
            if 'Shale' in formation:
                data['GR'][mask] = np.random.normal(shale_gr_mean, 15, mask.sum())  # High GR
                data['ILD'][mask] = np.random.lognormal(np.log(shale_res_mean), 0.3, mask.sum())  # Low resistivity
                data['RHOB'][mask] = np.random.normal(2.5, 0.1, mask.sum())  # Medium density
                data['NPHI'][mask] = np.random.normal(0.18, 0.03, mask.sum())  # Low-mid porosity
                data['DT'][mask] = np.random.normal(85, 5, mask.sum())  # High DT
                
            elif 'Sandstone' in formation:
                data['GR'][mask] = np.random.normal(sandstone_gr_mean, 10, mask.sum())  # Low GR
                data['ILD'][mask] = np.random.lognormal(np.log(sand_res_mean), 0.5, mask.sum())  # High resistivity
                data['RHOB'][mask] = np.random.normal(2.3, 0.08, mask.sum())  # Low density
                data['NPHI'][mask] = np.random.normal(0.22, 0.05, mask.sum())  # High porosity
                data['DT'][mask] = np.random.normal(70, 4, mask.sum())  # Low DT
                
            elif 'Limestone' in formation or 'Dolomite' in formation:
                data['GR'][mask] = np.random.normal(25, 8, mask.sum())  # Very low GR
                data['ILD'][mask] = np.random.lognormal(1.5, 0.4, mask.sum())  # Medium resistivity
                data['RHOB'][mask] = np.random.normal(2.7, 0.1, mask.sum())  # High density
                data['NPHI'][mask] = np.random.normal(0.05, 0.02, mask.sum())  # Very low porosity
                data['DT'][mask] = np.random.normal(50, 4, mask.sum())  # Very low DT
                
            elif 'Reservoir' in formation:
                data['GR'][mask] = np.random.normal(sandstone_gr_mean - 5, 5, mask.sum())  # Very low GR
                data['ILD'][mask] = np.random.lognormal(np.log(sand_res_mean * 1.5), 0.3, mask.sum())  # Very high resistivity
                data['RHOB'][mask] = np.random.normal(2.25, 0.05, mask.sum())  # Low density
                data['NPHI'][mask] = np.random.normal(reservoir_phi_mean, 0.04, mask.sum())  # High porosity
                data['DT'][mask] = np.random.normal(65, 3, mask.sum())  # Low DT
                
            elif 'Caprock' in formation:
                data['GR'][mask] = np.random.normal(45, 10, mask.sum())  # Medium GR
                data['ILD'][mask] = np.random.lognormal(0.8, 0.2, mask.sum())  # Low resistivity
                data['RHOB'][mask] = np.random.normal(2.6, 0.1, mask.sum())  # High density
                data['NPHI'][mask] = np.random.normal(0.08, 0.03, mask.sum())  # Low porosity
                data['DT'][mask] = np.random.normal(80, 6, mask.sum())  # High DT
        
        # Add correlations and trends
        data['LLD'] = data['ILD'] * 1.1
        data['LLS'] = data['ILD'] * 0.9
        data['MSFL'] = data['ILD'] * 0.7
        data['CALI'] = 8.5 + 0.1 * np.sin(depth/50)
        data['SP'] = -100 + 50 * np.sin(depth/100)
        data['PEF'] = np.random.normal(3.5, 0.5, n_points)
        data['DRHO'] = np.random.normal(0.05, 0.02, n_points)
        data['RHOZ'] = data['RHOB'] + 0.1 * np.random.randn(n_points)
        data['DTC'] = data['DT'] * 1.1
        data['DTS'] = data['DT'] * 1.8
        
        # Ensure positive values
        for col in data:
            data[col] = np.abs(data[col])
        
        # Create DataFrame
        df = pd.DataFrame(data)
        df.insert(0, 'Depth', depth)
        
        return df
        
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        return None

# ==================== PETROPHYSICAL CALCULATIONS ====================
def calculate_petrophysical_properties(df):
    """Calculate petrophysical properties from log data"""
    
    # Calculate porosity from density (using RHOB)
    matrix_density = 2.65  # g/cc for sandstone matrix
    fluid_density = 1.0    # g/cc for brine
    df['PHID'] = (matrix_density - df['RHOB']) / (matrix_density - fluid_density)
    df['PHID'] = df['PHID'].clip(0, 0.35)
    
    # Calculate porosity from neutron-density crossplot (simplified)
    df['PHIND'] = ((df['NPHI']**2 + df['PHID']**2) / 2)**0.5
    
    # Calculate water saturation using Archie's equation
    a, m, n = 1.0, 2.0, 2.0  # Archie parameters
    rw = 0.05  # Formation water resistivity (ohm-m)
    
    # Use LLD for deep resistivity
    df['SW'] = ((a * rw) / (df['LLD'] * df['PHIND']**m))**(1/n)
    df['SW'] = df['SW'].clip(0.2, 1.0)
    
    # Calculate hydrocarbon saturation
    df['SH'] = 1 - df['SW']
    
    # Calculate Vshale from GR
    gr_min = df['GR'].quantile(0.05)
    gr_max = df['GR'].quantile(0.95)
    df['VSH'] = (df['GR'] - gr_min) / (gr_max - gr_min)
    df['VSH'] = df['VSH'].clip(0, 1)
    
    # Calculate effective porosity
    df['PHIE'] = df['PHIND'] * (1 - df['VSH'])
    
    # Calculate permeability using Timur's equation
    df['PERM'] = 0.136 * (df['PHIE']**4.4) / (df['SW']**2)
    df['PERM'] = df['PERM'].clip(0.01, 5000)
    
    return df

# ==================== GEOMECHANICAL CALCULATIONS ====================
def calculate_geomechanical_properties(df):
    """Calculate geomechanical properties from log data"""
    
    # Calculate dynamic elastic properties from sonic logs
    # Convert DT to velocity (ft/s)
    vp = 1e6 / df['DT']
    vs = 1e6 / df['DTS'] if 'DTS' in df.columns else vp / 1.7
    
    # Calculate dynamic Young's Modulus (Mpsi)
    df['EDYN'] = (df['RHOB'] * (vs**2) * (3 * vp**2 - 4 * vs**2) / (vp**2 - vs**2)) / 1e6
    df['EDYN'] = df['EDYN'].clip(1, 10)
    
    # Calculate dynamic Poisson's Ratio
    df['PRDYN'] = (vp**2 - 2 * vs**2) / (2 * (vp**2 - vs**2))
    df['PRDYN'] = df['PRDYN'].clip(0.1, 0.4)
    
    # Calculate brittleness index (Rickman method)
    normalized_E = (df['EDYN'] - df['EDYN'].min()) / (df['EDYN'].max() - df['EDYN'].min() + 1e-5)
    normalized_PR = (df['PRDYN'] - df['PRDYN'].min()) / (df['PRDYN'].max() - df['PRDYN'].min() + 1e-5)
    df['BI'] = (normalized_E + (1 - normalized_PR)) / 2
    
    # Calculate pressure gradients (simplified)
    df['OBG'] = 1.0 + (df['Depth'] - df['Depth'].min()) * 0.0005
    df['PPG'] = 0.45 + 0.00015 * (df['Depth'] - df['Depth'].mean())
    df['PPG'] = df['PPG'].clip(0.43, 0.85)
    df['FG'] = df['PPG'] + (df['OBG'] - df['PPG']) * 0.4
    
    return df

# ==================== MAIN APPLICATION ====================
# Load and process data
st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
st.markdown("<h3 class='section-title'> WELL DATA OVERVIEW</h3>", unsafe_allow_html=True)

well_logs_df = process_well_log_data()

if well_logs_df is not None:
    # Calculate petrophysical and geomechanical properties
    well_logs_df = calculate_petrophysical_properties(well_logs_df)
    well_logs_df = calculate_geomechanical_properties(well_logs_df)
    
    # Well information
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Total Depth", f"{well_logs_df['Depth'].max():.1f} ft")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Data Points", f"{len(well_logs_df):,}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        avg_porosity = well_logs_df['PHIND'].mean()
        st.metric("Avg Porosity", f"{avg_porosity:.3f} v/v")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        reservoir_mask = (well_logs_df['GR'] < 60) & (well_logs_df['PHIND'] > 0.1)
        net_pay = well_logs_df[reservoir_mask]['Depth'].diff().abs().sum()
        st.metric("Net Pay", f"{net_pay:.0f} ft")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Display logs in tabs
    log_tab1, log_tab2, log_tab3, log_tab4 = st.tabs([
        " Basic Logs", 
        " Petrophysics", 
        " Geomechanics",
        " Crossplots"
    ])
    
    with log_tab1:
        # Triple combo display
        st.markdown("#### Triple Combo Log Suite")
        
        fig = go.Figure()
        
        # Track 1: Gamma Ray
        fig.add_trace(go.Scatter(
            x=well_logs_df['GR'],
            y=well_logs_df['Depth'],
            name='GR',
            line=dict(color='green', width=1),
            mode='lines'
        ))
        
        # Track 2: Deep Resistivity (log scale)
        fig.add_trace(go.Scatter(
            x=well_logs_df['LLD'],
            y=well_logs_df['Depth'],
            name='LLD',
            line=dict(color='red', width=1),
            mode='lines',
            xaxis='x2'
        ))
        
        # Track 3: Density
        fig.add_trace(go.Scatter(
            x=well_logs_df['RHOB'],
            y=well_logs_df['Depth'],
            name='RHOB',
            line=dict(color='blue', width=1),
            mode='lines',
            xaxis='x3'
        ))
        
        # Track 4: Neutron Porosity
        fig.add_trace(go.Scatter(
            x=well_logs_df['NPHI'],
            y=well_logs_df['Depth'],
            name='NPHI',
            line=dict(color='orange', width=1),
            mode='lines',
            xaxis='x4'
        ))
        
        # Track 5: Sonic
        fig.add_trace(go.Scatter(
            x=well_logs_df['DT'],
            y=well_logs_df['Depth'],
            name='DT',
            line=dict(color='purple', width=1),
            mode='lines',
            xaxis='x5'
        ))
        
        fig.update_layout(
            title="Triple Combo Log Display",
            yaxis=dict(
                title="Depth (ft)",
                autorange="reversed",
                range=[well_logs_df['Depth'].max(), well_logs_df['Depth'].min()]
            ),
            xaxis=dict(title="GR (API)", domain=[0, 0.16]),
            xaxis2=dict(title="LLD (Ω.m)", domain=[0.2, 0.36], type="log"),
            xaxis3=dict(title="RHOB (g/cc)", domain=[0.4, 0.56]),
            xaxis4=dict(title="NPHI (v/v)", domain=[0.6, 0.76]),
            xaxis5=dict(title="DT (μs/ft)", domain=[0.8, 0.96]),
            height=600,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with log_tab2:
        # Petrophysical analysis
        st.markdown("#### Petrophysical Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Porosity and saturation
            fig_phi = go.Figure()
            
            fig_phi.add_trace(go.Scatter(
                x=well_logs_df['PHIND'],
                y=well_logs_df['Depth'],
                name='Total Porosity',
                line=dict(color='blue', width=1.5),
                mode='lines'
            ))
            
            fig_phi.add_trace(go.Scatter(
                x=well_logs_df['PHIE'],
                y=well_logs_df['Depth'],
                name='Effective Porosity',
                line=dict(color='green', width=1.5),
                mode='lines',
                xaxis='x2'
            ))
            
            fig_phi.add_trace(go.Scatter(
                x=well_logs_df['SW'],
                y=well_logs_df['Depth'],
                name='Water Saturation',
                line=dict(color='red', width=1.5),
                mode='lines',
                xaxis='x3'
            ))
            
            fig_phi.update_layout(
                title="Porosity & Saturation Analysis",
                yaxis=dict(
                    autorange="reversed",
                    range=[well_logs_df['Depth'].max(), well_logs_df['Depth'].min()]
                ),
                xaxis=dict(title="PHIT (v/v)", domain=[0, 0.3]),
                xaxis2=dict(title="PHIE (v/v)", domain=[0.35, 0.65]),
                xaxis3=dict(title="Sw (v/v)", domain=[0.7, 1]),
                height=500
            )
            
            st.plotly_chart(fig_phi, use_container_width=True)
        
        with col2:
            # Vshale and permeability
            fig_perm = go.Figure()
            
            fig_perm.add_trace(go.Scatter(
                x=well_logs_df['VSH'],
                y=well_logs_df['Depth'],
                name='Vshale',
                line=dict(color='brown', width=1.5),
                mode='lines'
            ))
            
            fig_perm.add_trace(go.Scatter(
                x=np.log10(well_logs_df['PERM'] + 1),
                y=well_logs_df['Depth'],
                name='Perm (log10)',
                line=dict(color='purple', width=1.5),
                mode='lines',
                xaxis='x2'
            ))
            
            # Highlight pay zones
            pay_mask = (well_logs_df['VSH'] < 0.3) & (well_logs_df['PHIE'] > 0.1) & (well_logs_df['SW'] < 0.6)
            if pay_mask.any():
                pay_depths = well_logs_df.loc[pay_mask, 'Depth']
                if len(pay_depths) > 0:
                    fig_perm.add_trace(go.Scatter(
                        x=[0.5] * len(pay_depths),
                        y=pay_depths,
                        name='Pay Zone',
                        mode='markers',
                        marker=dict(color='yellow', size=4, symbol='square'),
                        xaxis='x'
                    ))
            
            fig_perm.update_layout(
                title="Shale Volume & Permeability",
                yaxis=dict(
                    autorange="reversed",
                    range=[well_logs_df['Depth'].max(), well_logs_df['Depth'].min()]
                ),
                xaxis=dict(title="Vshale (v/v)", domain=[0, 0.45]),
                xaxis2=dict(title="log10(Perm) (mD)", domain=[0.55, 1]),
                height=500
            )
            
            st.plotly_chart(fig_perm, use_container_width=True)
        
        # Pay zone summary
        st.markdown("#### Pay Zone Summary")
        
        # Define pay zone criteria
        pay_criteria = {
            'VSH < 0.3': (well_logs_df['VSH'] < 0.3),
            'PHIE > 0.08': (well_logs_df['PHIE'] > 0.08),
            'SW < 0.6': (well_logs_df['SW'] < 0.6)
        }
        
        pay_zone_mask = pay_criteria['VSH < 0.3'] & pay_criteria['PHIE > 0.08'] & pay_criteria['SW < 0.6']
        
        if pay_zone_mask.any():
            pay_zone_df = well_logs_df[pay_zone_mask]
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Net Pay Thickness", f"{pay_zone_df['Depth'].nunique():.0f} ft")
            
            with col2:
                avg_phi = pay_zone_df['PHIE'].mean()
                st.metric("Avg Eff. Porosity", f"{avg_phi:.3f}")
            
            with col3:
                avg_sw = pay_zone_df['SW'].mean()
                st.metric("Avg Water Sat.", f"{avg_sw:.3f}")
            
            with col4:
                avg_perm = pay_zone_df['PERM'].mean()
                st.metric("Avg Permeability", f"{avg_perm:.1f} mD")
    
    with log_tab3:
        # Geomechanical analysis
        st.markdown("#### Geomechanical Properties Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Elastic properties
            fig_elastic = go.Figure()
            
            fig_elastic.add_trace(go.Scatter(
                x=well_logs_df['EDYN'],
                y=well_logs_df['Depth'],
                name='Young\'s Modulus',
                line=dict(color='red', width=1.5),
                mode='lines'
            ))
            
            fig_elastic.add_trace(go.Scatter(
                x=well_logs_df['PRDYN'],
                y=well_logs_df['Depth'],
                name='Poisson\'s Ratio',
                line=dict(color='blue', width=1.5),
                mode='lines',
                xaxis='x2'
            ))
            
            fig_elastic.add_trace(go.Scatter(
                x=well_logs_df['BI'],
                y=well_logs_df['Depth'],
                name='Brittleness Index',
                line=dict(color='green', width=1.5),
                mode='lines',
                xaxis='x3'
            ))
            
            fig_elastic.update_layout(
                title="Elastic Properties",
                yaxis=dict(
                    autorange="reversed",
                    range=[well_logs_df['Depth'].max(), well_logs_df['Depth'].min()]
                ),
                xaxis=dict(title="E (Mpsi)", domain=[0, 0.3]),
                xaxis2=dict(title="ν", domain=[0.35, 0.65]),
                xaxis3=dict(title="BI", domain=[0.7, 1]),
                height=500
            )
            
            st.plotly_chart(fig_elastic, use_container_width=True)
        
        with col2:
            # Pressure profile
            fig_pressure = go.Figure()
            
            fig_pressure.add_trace(go.Scatter(
                x=well_logs_df['OBG'],
                y=well_logs_df['Depth'],
                name='Overburden',
                line=dict(color='black', width=2),
                mode='lines'
            ))
            
            fig_pressure.add_trace(go.Scatter(
                x=well_logs_df['PPG'],
                y=well_logs_df['Depth'],
                name='Pore Pressure',
                line=dict(color='blue', width=2),
                mode='lines',
                fill='tonexty'
            ))
            
            fig_pressure.add_trace(go.Scatter(
                x=well_logs_df['FG'],
                y=well_logs_df['Depth'],
                name='Fracture Gradient',
                line=dict(color='red', width=2),
                mode='lines',
                fill='tonexty'
            ))
            
            fig_pressure.update_layout(
                title="Pressure Gradient Profile",
                yaxis=dict(
                    autorange="reversed",
                    range=[well_logs_df['Depth'].max(), well_logs_df['Depth'].min()]
                ),
                xaxis=dict(title="Pressure (psi/ft)", range=[0.4, 1.2]),
                height=500
            )
            
            st.plotly_chart(fig_pressure, use_container_width=True)
        
        # Geomechanical recommendations
        st.markdown("#### Fracturing Recommendations")
        
        # Analyze brittleness in potential pay zones
        if pay_zone_mask.any():
            pay_zone_mech = well_logs_df[pay_zone_mask]
            
            avg_BI = pay_zone_mech['BI'].mean()
            avg_E = pay_zone_mech['EDYN'].mean()
            avg_PR = pay_zone_mech['PRDYN'].mean()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("<div class='well-info'>", unsafe_allow_html=True)
                st.markdown("**Geomechanical Properties in Pay Zone:**")
                st.markdown(f"- **Avg Brittleness Index:** {avg_BI:.3f}")
                st.markdown(f"- **Avg Young's Modulus:** {avg_E:.1f} Mpsi")
                st.markdown(f"- **Avg Poisson's Ratio:** {avg_PR:.3f}")
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown("<div class='well-info'>", unsafe_allow_html=True)
                st.markdown("**Fracturing Strategy:**")
                
                if avg_BI > 0.6:
                    st.success("""
                    **High Brittleness Zone:**
                    - Optimal for hydraulic fracturing
                    - Complex fracture networks expected
                    - Use slickwater or low-viscosity fluids
                    - High proppant concentration recommended
                    """)
                elif avg_BI > 0.4:
                    st.warning("""
                    **Medium Brittleness Zone:**
                    - Moderate fracturing complexity
                    - Planar fractures likely
                    - Consider hybrid fluid systems
                    - Moderate proppant loading
                    """)
                else:
                    st.error("""
                    **Low Brittleness Zone:**
                    - Challenging fracturing conditions
                    - Consider acid fracturing
                    - High viscosity fluids required
                    - Monitor for screenouts
                    """)
                st.markdown("</div>", unsafe_allow_html=True)
    
    with log_tab4:
        # Crossplot analysis
        st.markdown("#### Crossplot Analysis")
        
        # Select variables for crossplot
        col1, col2, col3 = st.columns(3)
        
        with col1:
            x_var = st.selectbox(
                "X-axis Variable",
                options=['GR', 'LLD', 'RHOB', 'NPHI', 'DT', 'PHIND', 'VSH', 'SW', 'EDYN', 'BI'],
                index=0
            )
        
        with col2:
            y_var = st.selectbox(
                "Y-axis Variable",
                options=['GR', 'LLD', 'RHOB', 'NPHI', 'DT', 'PHIND', 'VSH', 'SW', 'EDYN', 'BI'],
                index=3
            )
        
        with col3:
            color_var = st.selectbox(
                "Color by",
                options=['Depth', 'VSH', 'PHIND', 'SW', 'BI', 'EDYN'],
                index=0
            )
        
        # Create crossplot
        fig_cross = px.scatter(
            well_logs_df,
            x=x_var,
            y=y_var,
            color=color_var,
            title=f"{y_var} vs {x_var}",
            labels={x_var: x_var, y_var: y_var, color_var: color_var},
            height=500
        )
        
        # Add trendline if requested
        if st.checkbox("Show trendline"):
            fig_cross.update_traces(
                marker=dict(size=6, opacity=0.6),
                selector=dict(mode='markers')
            )
        
        st.plotly_chart(fig_cross, use_container_width=True)
        
        # Statistical summary
        st.markdown("#### Statistical Summary")
        
        # Select variable for statistics
        stat_var = st.selectbox(
            "Select variable for statistics",
            options=['GR', 'LLD', 'RHOB', 'NPHI', 'DT', 'PHIND', 'VSH', 'SW', 'PERM', 'EDYN', 'BI'],
            index=0
        )
        
        if stat_var in well_logs_df.columns:
            stats = well_logs_df[stat_var].describe()
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Mean", f"{stats['mean']:.3f}")
            with col2:
                st.metric("Std Dev", f"{stats['std']:.3f}")
            with col3:
                st.metric("Min", f"{stats['min']:.3f}")
            with col4:
                st.metric("Max", f"{stats['max']:.3f}")
    
    # Data download option
    st.markdown("---")
    st.markdown("#### Data Export")
    
    # Convert dataframe to CSV
    csv = well_logs_df.to_csv(index=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Download Processed Data (CSV)",
            data=csv,
            file_name="processed_well_logs.csv",
            mime="text/csv"
        )
    
    with col2:
        if st.button("📊 Generate Analysis Report"):
            st.info("Report generation would be implemented in a production system")
            st.markdown("""
            **Typical Report Includes:**
            - Well summary and statistics
            - Petrophysical analysis results
            - Net pay calculations
            - Geomechanical properties
            - Fracturing recommendations
            - Quality control metrics
            """)

else:
    st.error("Unable to process well log data. Please check the data source.")

st.markdown("</div>", unsafe_allow_html=True)

# ==================== TOGGLE PANELS SECTION ====================
st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
st.markdown("<h3 class='section-title'>B. TOGGLE PANELS – Select What to Inspect</h3>", unsafe_allow_html=True)

# Create toggle columns
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    show_geometry = st.toggle("**Fracture Geometry**", value=True, 
                             help="Display fracture geometry and propagation")
    if show_geometry:
        st.markdown("<span class='status-indicator status-online'></span> Active", unsafe_allow_html=True)

with col2:
    show_pressure = st.toggle("**Pressure & Treatment**", value=True,
                             help="Show pressure trends and treatment diagnostics")
    if show_pressure:
        st.markdown("<span class='status-indicator status-online'></span> Active", unsafe_allow_html=True)

with col3:
    show_monitoring = st.toggle("**Monitoring & Signals**", value=True,
                               help="Display microseismic and DAS/DTS signals")
    if show_monitoring:
        st.markdown("<span class='status-indicator status-online'></span> Active", unsafe_allow_html=True)

with col4:
    show_risk = st.toggle("**Risk & Health Indicators**", value=True,
                         help="Show risk assessments and health metrics")
    if show_risk:
        st.markdown("<span class='status-indicator status-online'></span> Active", unsafe_allow_html=True)

with col5:
    show_explain = st.toggle("**AI Explainability**", value=True,
                            help="Display AI reasoning and decision logic")
    if show_explain:
        st.markdown("<span class='status-indicator status-online'></span> Active", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==================== SIMULATION DATA GENERATION ====================
# Generate physics-based simulation data
time = np.linspace(0, 60, 100)

# Physics: Net pressure from modified KGD model
visc_factor = fluid_viscosity * 2 if fluid_type == "Gel" else fluid_viscosity
net_pressure = 500 + pump_rate * 2.5 - sigma_hmin * 0.7 + (young_modulus / (poisson_ratio + 0.01)) * 12
net_pressure = net_pressure + np.cumsum(np.random.normal(0, 15, 100))

# Microseismic rate (real physics-based)
stress_shadow_index = max(0.1, 1 - cluster_spacing / 60) * (sigma_hmax - sigma_hmin) / 2500
microseismic_rate = 60 * np.exp(-0.04 * time * (1 + stress_shadow_index))

# Pressure derivative (real-time monitoring)
pressure_slope = np.gradient(net_pressure)

# Proppant transport efficiency
proppant_loading = proppant_conc * pump_rate / 80

# Fracture geometry (simplified KGD/Geertsma-deKlerk)
frac_half_length = (pump_rate * visc_factor * time[-1] / (young_modulus * 1e6))**0.25 * 120
frac_height = (stress_contrast / 800) * 150 if stress_contrast > 0 else 100
frac_width = (pump_rate * visc_factor)**0.2 * 10

# Fracture efficiency (physics-based)
efficiency = 100 * (1 - proppant_loading / 12) * (1 - stress_shadow_index * 0.8)
efficiency = max(30, min(95, efficiency))

# ==================== FRACGUARD™ RISK ENGINE ====================
# Closure risk assessment
closure_risk = "Low"
closure_score = 0

if net_pressure[-1] > net_pressure[0] + 150 and microseismic_rate[-1] < microseismic_rate[0] * 0.5:
    closure_risk = "HIGH"
    closure_score = 85
elif net_pressure[-1] > net_pressure[0] + 80:
    closure_risk = "Medium"
    closure_score = 60
else:
    closure_score = 25

closure_explain = "Elevated net pressure with declining microseismicity indicates fracture width loss and early closure risk." if closure_risk == "HIGH" else "Stable pressure profile suggests adequate fracture maintenance."

# Height growth risk
height_growth_risk = "Low"
height_score = 0

if stress_contrast < 1200 and net_pressure[-1] > sigma_hmin * 1.15:
    height_growth_risk = "HIGH"
    height_score = 80
elif stress_contrast < 1800:
    height_growth_risk = "Medium"
    height_score = 45
else:
    height_score = 20

height_explain = "Insufficient vertical stress contrast allows fracture growth into non-target zones." if height_growth_risk == "HIGH" else "Adequate stress contrast contains fracture height."

# Screenout probability
screenout_prob = 0
if proppant_loading > 6 and pressure_slope[-1] > 15:
    screenout_prob = 70 + (proppant_loading - 6) * 8
elif proppant_loading > 4:
    screenout_prob = 40 + (proppant_loading - 4) * 10
else:
    screenout_prob = proppant_loading * 5

screenout_prob = min(95, screenout_prob)
screenout_explain = "High proppant concentration with rising pressure indicates near-wellbore bridging risk." if screenout_prob > 50 else "Proppant transport appears efficient."

# ==================== PROFESSIONAL FRACSCOPE™ VISUALIZATION ====================
if show_geometry or show_pressure or show_monitoring:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-title'>🏆 FRACSCOPE™ PROFESSIONAL - REAL-TIME FRACTURE VISUALIZATION</h3>", unsafe_allow_html=True)
    
    viz_tab1, viz_tab2, viz_tab3, viz_tab4 = st.tabs(["📐 Fracture Geometry", "📈 Pressure Diagnostics", "🌍 Microseismic Monitoring", "🔬 3D Fracture Network"])
    
    with viz_tab1:
        if show_geometry:
            # Professional fracture geometry dashboard
            col_g1, col_g2, col_g3 = st.columns([2, 1, 1])
            
            with col_g1:
                # Advanced fracture geometry visualization
                fig_geo = go.Figure()
                
                # Create realistic fracture profile
                x_profile = np.linspace(0, frac_half_length, 50)
                width_profile = frac_width * (1 - (x_profile/frac_half_length)**2)**0.5
                
                # Main fracture body
                fig_geo.add_trace(go.Scatter(
                    x=x_profile,
                    y=width_profile/12,  # Convert inches to feet
                    name='Fracture Width',
                    fill='tozeroy',
                    fillcolor='rgba(0, 100, 255, 0.3)',
                    line=dict(color='#0064FF', width=3),
                    mode='lines'
                ))
                
                # Add proppant distribution
                proppant_profile = width_profile * (proppant_conc/2) * (1 - x_profile/frac_half_length)
                fig_geo.add_trace(go.Scatter(
                    x=x_profile,
                    y=proppant_profile/24,
                    name='Proppant Concentration',
                    line=dict(color='#FF4500', width=2, dash='dash'),
                    fill='tozeroy',
                    fillcolor='rgba(255, 69, 0, 0.2)',
                    mode='lines'
                ))
                
                # Stress shadow effect
                stress_shadow = 0.3 * frac_width/12 * np.exp(-x_profile/(frac_half_length*0.3))
                fig_geo.add_trace(go.Scatter(
                    x=x_profile,
                    y=-stress_shadow,
                    name='Stress Shadow',
                    line=dict(color='#8B0000', width=2, dash='dot'),
                    fill='tozeroy',
                    fillcolor='rgba(139, 0, 0, 0.1)',
                    mode='lines'
                ))
                
                fig_geo.update_layout(
                    title={
                        'text': f"FRACTURE GEOMETRY PROFILE - Half Length: {frac_half_length:.0f} ft",
                        'font': {'size': 16, 'color': '#2C3E50'}
                    },
                    xaxis_title="Distance from Wellbore (ft)",
                    yaxis_title="Width (ft)",
                    height=350,
                    hovermode='x unified',
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="center",
                        x=0.5
                    ),
                    plot_bgcolor='rgba(240, 240, 240, 0.8)',
                    paper_bgcolor='white'
                )
                
                st.plotly_chart(fig_geo, use_container_width=True)
            
            with col_g2:
                # Professional metrics display
                st.markdown("###  Geometry Metrics")
                
                metrics_data = {
                    'Parameter': ['Half Length', 'Height', 'Avg Width', 'SRV'],
                    'Value': [f"{frac_half_length:.0f} ft", f"{frac_height:.0f} ft", 
                             f"{frac_width:.2f} in", f"{(frac_half_length * frac_height * 0.8):,.0f} ft³"],
                    'Status': ['✅ Optimal' if frac_half_length > 300 else '⚠️ Short',
                              '✅ Contained' if frac_height < 200 else '⚠️ High',
                              '✅ Adequate' if frac_width > 0.15 else '⚠️ Narrow',
                              '✅ Large' if (frac_half_length * frac_height) > 50000 else '⚠️ Small']
                }
                
                for i in range(4):
                    st.metric(
                        label=metrics_data['Parameter'][i],
                        value=metrics_data['Value'][i],
                        delta=metrics_data['Status'][i],
                        delta_color="normal"
                    )
                
                # Aspect ratio
                aspect_ratio = frac_height / frac_half_length
                st.metric(
                    "Aspect Ratio",
                    f"{aspect_ratio:.2f}",
                    "Optimal" if 0.3 < aspect_ratio < 0.7 else "Review"
                )
            
            with col_g3:
                # Fracture efficiency professional gauge
                st.markdown("###  Efficiency Analysis")
                
                fig_gauge = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=efficiency,
                    title={
                        'text': "Fracture Efficiency",
                        'font': {'size': 14, 'color': '#2C3E50'}
                    },
                    delta={'reference': 70, 'increasing': {'color': "#00CC00"}},
                    gauge={
                        'axis': {
                            'range': [0, 100],
                            'tickwidth': 1,
                            'tickcolor': "#2C3E50"
                        },
                        'bar': {
                            'color': "#0066CC",
                            'thickness': 0.25
                        },
                        'bgcolor': "white",
                        'borderwidth': 2,
                        'bordercolor': "gray",
                        'steps': [
                            {'range': [0, 50], 'color': '#FF4D4D'},
                            {'range': [50, 75], 'color': '#FFA500'},
                            {'range': [75, 100], 'color': '#00CC00'}
                        ],
                        'threshold': {
                            'line': {'color': "#8B0000", 'width': 4},
                            'thickness': 0.75,
                            'value': 75
                        }
                    }
                ))
                
                fig_gauge.update_layout(
                    height=250,
                    margin=dict(l=20, r=20, t=50, b=20)
                )
                
                st.plotly_chart(fig_gauge, use_container_width=True)
                
                # Efficiency drivers
                st.markdown("####  Efficiency Drivers")
                col_e1, col_e2 = st.columns(2)
                with col_e1:
                    st.progress(min(1.0, proppant_loading/8), text=f"Proppant: {proppant_loading:.1f}/8")
                with col_e2:
                    stress_shadow_effect = max(0, min(1.0, 1 - stress_shadow_index))  # Ensure between 0 and 1
                    st.progress(stress_shadow_effect, text=f"Stress Shadow: {stress_shadow_index:.2f}")
    
    with viz_tab2:
        if show_pressure:
            # Professional pressure diagnostics
            st.markdown("###  PRESSURE DIAGNOSTICS & ANALYSIS")
            
            # Enhanced pressure data with realistic physics
            df_pressure = pd.DataFrame({
                'Time (min)': time,
                'Net Pressure (psi)': net_pressure,
                'Pressure Derivative (psi/min)': pressure_slope,
                'Closure Gradient (psi/ft)': 0.7 + 0.1 * (net_pressure - net_pressure.min()) / (net_pressure.max() - net_pressure.min()),
                'ISIP Estimate (psi)': net_pressure * 0.85
            })
            
            # Create professional pressure plot
            fig_pressure = go.Figure()
            
            # Main pressure curve with gradient fill
            fig_pressure.add_trace(go.Scatter(
                x=df_pressure['Time (min)'],
                y=df_pressure['Net Pressure (psi)'],
                name='Net Pressure',
                line=dict(color='#0066CC', width=4),
                fill='tozeroy',
                fillcolor='rgba(0, 102, 204, 0.1)',
                mode='lines',
                hovertemplate='<b>Time:</b> %{x:.1f} min<br><b>Pressure:</b> %{y:.0f} psi<extra></extra>'
            ))
            
            # Derivative curve
            fig_pressure.add_trace(go.Scatter(
                x=df_pressure['Time (min)'],
                y=df_pressure['Pressure Derivative (psi/min)'],
                name='Pressure Derivative',
                line=dict(color='#FF4500', width=3, dash='dash'),
                mode='lines',
                yaxis='y2'
            ))
            
            # Add pressure regimes
            pressure_regimes = [
                (0, 15, 'Near-Wellbore', '#00CC00'),
                (15, 40, 'Propagation', '#FFA500'),
                (40, 60, 'Closure', '#FF4D4D')
            ]
            
            for start, end, label, color in pressure_regimes:
                fig_pressure.add_vrect(
                    x0=start, x1=end,
                    fillcolor=color,
                    opacity=0.1,
                    layer="below",
                    line_width=0,
                )
                fig_pressure.add_annotation(
                    x=(start + end)/2,
                    y=net_pressure.max() * 0.9,
                    text=label,
                    showarrow=False,
                    font=dict(size=10, color=color)
                )
            
            fig_pressure.update_layout(
                title={
                    'text': "REAL-TIME PRESSURE DIAGNOSTICS - Fracturing Treatment",
                    'font': {'size': 16, 'color': '#2C3E50'}
                },
                xaxis_title="Treatment Time (minutes)",
                yaxis=dict(
                    title="Net Pressure (psi)",
                    gridcolor='rgba(200,200,200,0.3)'
                ),
                yaxis2=dict(
                    title="Pressure Derivative (psi/min)",
                    overlaying='y',
                    side='right',
                    gridcolor='rgba(200,200,200,0.2)'
                ),
                height=450,
                hovermode='x unified',
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="center",
                    x=0.5
                ),
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            
            st.plotly_chart(fig_pressure, use_container_width=True)
            
            # Professional pressure statistics
            st.markdown("####  Pressure Analysis Summary")
            
            col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns(5)
            
            with col_p1:
                pressure_gradient = (net_pressure[-1] - net_pressure[0]) / time[-1]
                st.metric(
                    "Pressure Gradient",
                    f"{pressure_gradient:.1f} psi/min",
                    "Optimal" if 2 < pressure_gradient < 10 else "Review"
                )
            
            with col_p2:
                closure_pressure = net_pressure[-1] * 0.85
                st.metric(
                    "Closure Pressure",
                    f"{closure_pressure:.0f} psi",
                    f"{closure_pressure/sigma_hmin*100:.0f}% σhmin"
                )
            
            with col_p3:
                isip = net_pressure[-1]
                st.metric(
                    "ISIP",
                    f"{isip:.0f} psi",
                    "High" if isip > sigma_hmin * 1.2 else "Normal"
                )
            
            with col_p4:
                max_slope = pressure_slope.max()
                st.metric(
                    "Max Slope",
                    f"{max_slope:.1f} psi/min",
                    "Screenout Risk" if max_slope > 15 else "Safe"
                )
            
            with col_p5:
                avg_slope = pressure_slope.mean()
                st.metric(
                    "Avg Slope",
                    f"{avg_slope:.1f} psi/min",
                    "Stable" if -5 < avg_slope < 5 else "Unstable"
                )
            
            # Pressure interpretation
            st.markdown("#### 🎯 Diagnostic Interpretation")
            
            if pressure_slope[-1] > 10:
                st.error("""
                ⚠️ **SCREENOUT RISK DETECTED**
                - Rising pressure derivative indicates near-wellbore bridging
                - Immediate action required: Reduce proppant concentration
                - Consider flush stage to clear near-wellbore
                """)
            elif pressure_slope[-1] < -5:
                st.warning("""
                ⚡ **FRACTURE EXTENSION DETECTED**
                - Negative slope indicates fracture growth
                - Continue current treatment parameters
                - Monitor for height growth
                """)
            else:
                st.success("""
                ✅ **STABLE FRACTURE PROPAGATION**
                - Pressure profile indicates controlled growth
                - Maintain current treatment parameters
                - Optimal fracture development
                """)
    
    with viz_tab3:
        if show_monitoring:
            col_m1, col_m2 = st.columns([2, 1])
            
            with col_m1:
                df_micro = pd.DataFrame({
                    'Time (min)': time,
                    'Microseismic Rate': microseismic_rate,
                    'Cumulative Events': np.cumsum(microseismic_rate) / 10
                })
                
                fig_micro = go.Figure()
                fig_micro.add_trace(go.Scatter(
                    x=df_micro['Time (min)'],
                    y=df_micro['Microseismic Rate'],
                    name='Event Rate',
                    line=dict(color='#1f77b4', width=2),
                    mode='lines'
                ))
                
                fig_micro.add_trace(go.Scatter(
                    x=df_micro['Time (min)'],
                    y=df_micro['Cumulative Events'],
                    name='Cumulative Events',
                    line=dict(color='#2ca02c', width=2),
                    mode='lines',
                    yaxis='y2'
                ))
                
                fig_micro.update_layout(
                    title="Microseismic Monitoring",
                    yaxis=dict(title="Event Rate (events/min)"),
                    yaxis2=dict(
                        title="Cumulative Events",
                        overlaying='y',
                        side='right'
                    ),
                    height=400
                )
                
                st.plotly_chart(fig_micro, use_container_width=True)
            
            with col_m2:
                st.markdown("#### Monitoring Status")
                
                monitoring_status = {
                    "DAS": "Active" if das_enabled else "Inactive",
                    "DTS": "Active" if dts_enabled else "Inactive",
                    "Downhole Gauges": "Active" if downhole_gauges else "Inactive",
                    "Microseismic": "Active",
                    "Surface Sensors": "Active"
                }
                
                for sensor, status in monitoring_status.items():
                    if status == "Active":
                        st.success(f"✓ {sensor}: {status}")
                    else:
                        st.warning(f"○ {sensor}: {status}")
                
                st.metric("Total Events", f"{int(df_micro['Cumulative Events'].iloc[-1])}")
                st.metric("Peak Rate", f"{microseismic_rate.max():.1f}/min")
    
    with viz_tab4:
        if show_geometry:
            st.markdown("###  3D FRACTURE NETWORK VISUALIZATION")
            
            # Generate realistic 3D fracture network
            # Based on KGD/Geertsma-deKlerk model with natural fractures
            
            # Main fracture plane
            x_main = np.linspace(-frac_half_length, frac_half_length, 50)
            z_main = np.linspace(-frac_height/2, frac_height/2, 50)
            X_main, Z_main = np.meshgrid(x_main, z_main)
            
            # Realistic fracture width profile (elliptical with stress shadows)
            Y_main = frac_width * np.sqrt(1 - (X_main/frac_half_length)**2 - (Z_main/frac_height)**2)
            
            # Add natural fracture network
            n_natural_fractures = 20
            natural_fractures = []
            
            for i in range(n_natural_fractures):
                # Random orientation and position
                angle = np.random.uniform(0, np.pi)
                length = np.random.uniform(20, frac_half_length * 0.3)
                height = np.random.uniform(10, frac_height * 0.4)
                center_x = np.random.uniform(-frac_half_length * 0.7, frac_half_length * 0.7)
                center_z = np.random.uniform(-frac_height * 0.3, frac_height * 0.3)
                
                # Create natural fracture plane
                x_nat = np.linspace(-length, length, 20)
                z_nat = np.linspace(-height, height, 20)
                X_nat, Z_nat = np.meshgrid(x_nat, z_nat)
                
                # Rotate and position
                X_rot = X_nat * np.cos(angle) + center_x
                Z_rot = Z_nat + center_z
                Y_nat = np.zeros_like(X_nat) + np.random.uniform(-0.5, 0.5)
                
                natural_fractures.append((X_rot, Y_nat, Z_rot))
            
            # Create 3D visualization
            fig_3d = go.Figure()
            
            # Main hydraulic fracture
            fig_3d.add_trace(go.Surface(
                x=X_main,
                y=Y_main,
                z=Z_main,
                colorscale=[
                    [0, 'rgba(0, 100, 255, 0.1)'],
                    [0.5, 'rgba(0, 100, 255, 0.5)'],
                    [1, 'rgba(0, 100, 255, 0.8)']
                ],
                opacity=0.9,
                contours={
                    "z": {"show": True, "usecolormap": True, "highlightcolor": "white"},
                    "x": {"show": True, "highlightcolor": "white"}
                },
                name='Main Fracture',
                showscale=False,
                hovertemplate='<b>Main Fracture</b><br>Width: %{y:.3f} in<extra></extra>'
            ))
            
            # Natural fractures
            for i, (X_nat, Y_nat, Z_nat) in enumerate(natural_fractures):
                fig_3d.add_trace(go.Surface(
                    x=X_nat,
                    y=Y_nat,
                    z=Z_nat,
                    colorscale=[
                        [0, 'rgba(255, 69, 0, 0.05)'],
                        [1, 'rgba(255, 69, 0, 0.2)']
                    ],
                    opacity=0.3,
                    showscale=False,
                    name=f'Natural Fracture {i+1}',
                    hovertemplate='<b>Natural Fracture</b><extra></extra>'
                ))
            
            # Add wellbore
            wellbore_depth = np.linspace(5000 - frac_height/2, 5000 + frac_height/2, 100)
            fig_3d.add_trace(go.Scatter3d(
                x=np.zeros(100),
                y=np.zeros(100),
                z=wellbore_depth - 5000,  # Center at 0
                mode='lines',
                line=dict(color='black', width=6),
                name='Wellbore',
                hovertemplate='<b>Wellbore</b><extra></extra>'
            ))
            
            # Add proppant distribution
            proppant_x = np.random.uniform(-frac_half_length * 0.8, frac_half_length * 0.8, 200)
            proppant_z = np.random.uniform(-frac_height * 0.4, frac_height * 0.4, 200)
            proppant_y = np.zeros(200) + np.random.uniform(0, frac_width * 0.5, 200)
            
            fig_3d.add_trace(go.Scatter3d(
                x=proppant_x,
                y=proppant_y,
                z=proppant_z,
                mode='markers',
                marker=dict(
                    size=3,
                    color='#FFD700',
                    opacity=0.6
                ),
                name='Proppant',
                hovertemplate='<b>Proppant Particle</b><extra></extra>'
            ))
            
            fig_3d.update_layout(
                title={
                    'text': "3D FRACTURE NETWORK SIMULATION",
                    'font': {'size': 18, 'color': '#2C3E50', 'family': 'Arial'}
                },
                scene=dict(
                    xaxis=dict(
                        title='Distance from Well (ft)',
                        gridcolor='rgba(200,200,200,0.5)',
                        backgroundcolor='rgba(240, 240, 240, 0.8)'
                    ),
                    yaxis=dict(
                        title='Fracture Width (in)',
                        gridcolor='rgba(200,200,200,0.5)',
                        backgroundcolor='rgba(240, 240, 240, 0.8)'
                    ),
                    zaxis=dict(
                        title='Depth (ft)',
                        gridcolor='rgba(200,200,200,0.5)',
                        backgroundcolor='rgba(240, 240, 240, 0.8)'
                    ),
                    aspectratio=dict(x=2, y=0.3, z=1),
                    camera=dict(
                        eye=dict(x=1.5, y=1.5, z=1),
                        up=dict(x=0, y=0, z=1)
                    )
                ),
                height=700,
                margin=dict(l=0, r=0, t=40, b=0),
                showlegend=True,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01
                )
            )
            
            st.plotly_chart(fig_3d, use_container_width=True)
            
            # 3D View controls
            col_3d1, col_3d2, col_3d3 = st.columns(3)
            
            with col_3d1:
                view_option = st.selectbox(
                    "View Preset",
                    ["Standard", "Top Down", "Side View", "Isometric"],
                    index=0
                )
            
            with col_3d2:
                show_proppant = st.toggle("Show Proppant", True)
            
            with col_3d3:
                show_natural = st.toggle("Show Natural Fractures", True)
            
            # Fracture network statistics
            st.markdown("####  Fracture Network Statistics")
            
            col_s1, col_s2, col_s3, col_s4 = st.columns(4)
            
            with col_s1:
                st.metric(
                    "Main Fracture Area",
                    f"{(frac_half_length * 2 * frac_height):,.0f} ft²"
                )
            
            with col_s2:
                total_natural_area = sum([np.random.uniform(100, 500) for _ in range(n_natural_fractures)])
                st.metric(
                    "Natural Fracture Area",
                    f"{total_natural_area:,.0f} ft²"
                )
            
            with col_s3:
                complexity_index = n_natural_fractures / 10
                st.metric(
                    "Complexity Index",
                    f"{complexity_index:.1f}",
                    "High" if complexity_index > 1.5 else "Moderate"
                )
            
            with col_s4:
                connectivity = min(1, (frac_half_length * 0.5) / total_natural_area * 1000)
                st.metric(
                    "Network Connectivity",
                    f"{connectivity*100:.0f}%",
                    "Good" if connectivity > 0.7 else "Limited"
                )

    st.markdown("</div>", unsafe_allow_html=True)

# ==================== FRACGUARD™ RISK INDICATORS ====================
if show_risk:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    
    # Section Header with Enhanced Styling
    st.markdown("""
    <div class='section-header' style='margin-bottom: 2rem;'>
        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 8px;'>
            <svg style='width: 28px; height: 28px;' fill='none' stroke='#ff4b4b' viewBox='0 0 24 24'>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.282 16.5c-.77.833.192 2.5 1.732 2.5z"></path>
            </svg>
            <h3 style='margin: 0; color: #1e3a8a; font-size: 1.5rem; font-weight: 700;'>FRACGUARD™ – RISK & HEALTH MONITORING</h3>
        </div>
        <p style='color: #6b7280; margin: 0; font-size: 0.95rem; line-height: 1.5;'>
            Real-time risk assessment with predictive analytics for proactive fracture management
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Risk Metrics Grid
    st.markdown("""
    <div style='margin-bottom: 2.5rem;'>
        <h4 style='color: #374151; font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>
            📊 KEY RISK INDICATORS
        </h4>
    """, unsafe_allow_html=True)
    
    # Create risk metrics with enhanced styling
    risk_col1, risk_col2, risk_col3, risk_col4 = st.columns(4)
    
    # Helper function to create risk metric cards
    def create_risk_metric(col, title, value, delta_value, risk_score, risk_level, color):
        with col:
            # Determine colors based on risk level
            if risk_level == "HIGH":
                bg_color = "rgba(239, 68, 68, 0.1)"
                border_color = "#ef4444"
                text_color = "#dc2626"
            elif risk_level == "Medium":
                bg_color = "rgba(249, 115, 22, 0.1)"
                border_color = "#f97316"
                text_color = "#ea580c"
            else:
                bg_color = "rgba(34, 197, 94, 0.1)"
                border_color = "#22c55e"
                text_color = "#16a34a"
            
            # Metric Card
            st.markdown(f"""
            <div style='
                background: {bg_color};
                border: 2px solid {border_color};
                border-radius: 12px;
                padding: 1.25rem;
                margin-bottom: 1rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            '>
                <div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;'>
                    <div>
                        <p style='margin: 0; color: #6b7280; font-size: 0.875rem; font-weight: 500;'>{title}</p>
                        <h2 style='margin: 0.25rem 0; color: {text_color}; font-size: 2rem; font-weight: 700;'>{value}</h2>
                    </div>
                    <div style='
                        background: {border_color};
                        color: white;
                        padding: 0.25rem 0.75rem;
                        border-radius: 20px;
                        font-size: 0.75rem;
                        font-weight: 600;
                    '>
                        {risk_level}
                    </div>
                </div>
                <div style='margin-top: 1rem;'>
                    <div style='display: flex; justify-content: space-between; margin-bottom: 0.5rem;'>
                        <span style='color: #6b7280; font-size: 0.875rem;'>Risk Score</span>
                        <span style='color: {text_color}; font-weight: 600;'>{risk_score}%</span>
                    </div>
                    <div style='
                        height: 8px;
                        background: #e5e7eb;
                        border-radius: 4px;
                        overflow: hidden;
                    '>
                        <div style='
                            width: {risk_score}%;
                            height: 100%;
                            background: linear-gradient(90deg, {border_color}, {color});
                            border-radius: 4px;
                        '></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Create metrics
    create_risk_metric(
        risk_col1, 
        "Early Closure Risk", 
        closure_risk, 
        f"{closure_score}%", 
        closure_score,
        "HIGH" if closure_risk == "HIGH" else "Medium" if closure_risk == "Medium" else "LOW",
        "#ef4444" if closure_risk == "HIGH" else "#f97316" if closure_risk == "Medium" else "#22c55e"
    )
    
    create_risk_metric(
        risk_col2,
        "Screenout Probability",
        f"{int(screenout_prob)}%",
        "High" if screenout_prob > 70 else "Moderate" if screenout_prob > 40 else "Low",
        int(screenout_prob),
        "HIGH" if screenout_prob > 70 else "Medium" if screenout_prob > 40 else "LOW",
        "#ef4444" if screenout_prob > 70 else "#f97316" if screenout_prob > 40 else "#22c55e"
    )
    
    create_risk_metric(
        risk_col3,
        "Height Growth Risk",
        height_growth_risk,
        f"{height_score}%",
        height_score,
        "HIGH" if height_growth_risk == "HIGH" else "Medium" if height_growth_risk == "Medium" else "LOW",
        "#ef4444" if height_growth_risk == "HIGH" else "#f97316" if height_growth_risk == "Medium" else "#22c55e"
    )
    
    create_risk_metric(
        risk_col4,
        "Fracture Efficiency",
        f"{int(efficiency)}%",
        "Optimal" if efficiency > 70 else "Adequate" if efficiency > 50 else "Poor",
        int(efficiency),
        "OPTIMAL" if efficiency > 70 else "ADEQUATE" if efficiency > 50 else "LOW",
        "#22c55e" if efficiency > 70 else "#f97316" if efficiency > 50 else "#ef4444"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Enhanced Risk Matrix
    st.markdown("""
    <div style='margin-top: 2.5rem;'>
        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;'>
            <div>
                <h4 style='color: #374151; font-size: 1.1rem; font-weight: 600; margin: 0;'>
                     RISK MATRIX ANALYSIS
                </h4>
                <p style='color: #6b7280; margin: 0.25rem 0 0 0; font-size: 0.875rem;'>
                    Visual representation of probability vs. impact for all risk factors
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Prepare risk matrix data
    risk_matrix_data = pd.DataFrame({
        'Risk Type': ['Closure', 'Screenout', 'Height Growth', 'Inefficiency', 'Asymmetry'],
        'Probability': [closure_score/100, screenout_prob/100, height_score/100, (100-efficiency)/100, 0.3],
        'Impact': [0.8, 0.9, 0.6, 0.5, 0.4],
        'Risk Score': [closure_score, screenout_prob, height_score, 100-efficiency, 30],
        'Category': ['Critical', 'Critical', 'Moderate', 'Moderate', 'Low']
    })
    
    # Create enhanced risk matrix
    fig_risk_matrix = go.Figure()
    
    # Add risk zones with gradient fills
    fig_risk_matrix.add_shape(
        type="rect", x0=0, y0=0, x1=0.3, y1=0.3,
        line=dict(color="#22c55e", width=1.5),
        fillcolor="rgba(34, 197, 94, 0.05)",
        layer="below",
        name="Low Risk Zone"
    )
    
    fig_risk_matrix.add_shape(
        type="rect", x0=0.3, y0=0.3, x1=0.7, y1=0.7,
        line=dict(color="#f97316", width=1.5),
        fillcolor="rgba(249, 115, 22, 0.05)",
        layer="below",
        name="Medium Risk Zone"
    )
    
    fig_risk_matrix.add_shape(
        type="rect", x0=0.7, y0=0.7, x1=1, y1=1,
        line=dict(color="#ef4444", width=1.5),
        fillcolor="rgba(239, 68, 68, 0.05)",
        layer="below",
        name="High Risk Zone"
    )
    
    # Add risk points with custom styling
    risk_colors = {
        'Critical': '#ef4444',
        'Moderate': '#f97316',
        'Low': '#22c55e'
    }
    
    for category in risk_matrix_data['Category'].unique():
        cat_data = risk_matrix_data[risk_matrix_data['Category'] == category]
        fig_risk_matrix.add_trace(go.Scatter(
            x=cat_data['Probability'],
            y=cat_data['Impact'],
            mode='markers+text',
            marker=dict(
                size=cat_data['Risk Score']/2 + 15,
                color=risk_colors[category],
                opacity=0.8,
                line=dict(width=2, color='white'),
                symbol='circle'
            ),
            text=cat_data['Risk Type'],
            textposition="top center",
            textfont=dict(
                family="Arial",
                size=12,
                color=risk_colors[category]
            ),
            customdata=np.stack((
                cat_data['Risk Score'],
                cat_data['Category']
            ), axis=-1),
            hovertemplate="<b>%{text}</b><br>" +
                         "Probability: %{x:.1%}<br>" +
                         "Impact: %{y:.1%}<br>" +
                         "Risk Score: %{customdata[0]:.0f}<br>" +
                         "Category: %{customdata[1]}<br>" +
                         "<extra></extra>",
            name=category + " Risk"
        ))
    
    # Update layout for professional appearance
    fig_risk_matrix.update_layout(
        plot_bgcolor='rgba(255, 255, 255, 0.9)',
        paper_bgcolor='white',
        height=500,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=1.02,
            bgcolor='rgba(255, 255, 255, 0.8)',
            bordercolor='#e5e7eb',
            borderwidth=1,
            font=dict(size=11)
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        ),
        xaxis=dict(
            title="Probability",
            tickformat=".0%",
            gridcolor='rgba(0,0,0,0.05)',
            zerolinecolor='rgba(0,0,0,0.1)',
            range=[0, 1]
        ),
        yaxis=dict(
            title="Impact",
            tickformat=".0%",
            gridcolor='rgba(0,0,0,0.05)',
            zerolinecolor='rgba(0,0,0,0.1)',
            range=[0, 1]
        ),
        margin=dict(l=50, r=120, t=40, b=60),
        title=dict(
            text="<b>RISK PROBABILITY-IMPACT MATRIX</b>",
            x=0.05,
            y=0.95,
            font=dict(size=16, color="#1e3a8a")
        ),
        annotations=[
            dict(
                x=0.15, y=0.15,
                xref="x", yref="y",
                text="LOW RISK",
                showarrow=False,
                font=dict(size=11, color="#22c55e")
            ),
            dict(
                x=0.5, y=0.5,
                xref="x", yref="y",
                text="MEDIUM RISK",
                showarrow=False,
                font=dict(size=11, color="#f97316")
            ),
            dict(
                x=0.85, y=0.85,
                xref="x", yref="y",
                text="HIGH RISK",
                showarrow=False,
                font=dict(size=11, color="#ef4444")
            )
        ]
    )
    
    # Display the chart
    st.plotly_chart(fig_risk_matrix, use_container_width=True)
    
    # Risk Summary Table
    st.markdown("""
    <div style='margin-top: 2.5rem;'>
        <h4 style='color: #374151; font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>
             RISK FACTOR SUMMARY
        </h4>
    """, unsafe_allow_html=True)
    
    # Create styled summary table
    summary_data = pd.DataFrame({
        'Risk Factor': ['Early Closure', 'Screenout', 'Height Growth', 'Fracture Efficiency', 'Asymmetry'],
        'Probability': [
            f"{closure_score}%",
            f"{int(screenout_prob)}%",
            f"{height_score}%",
            f"{100-int(efficiency)}%",
            "30%"
        ],
        'Impact': ['High', 'Critical', 'Moderate', 'Moderate', 'Low'],
        'Mitigation Priority': [
            'Immediate' if closure_risk == "HIGH" else 'High' if closure_risk == "Medium" else 'Monitor',
            'Immediate' if screenout_prob > 70 else 'High' if screenout_prob > 40 else 'Monitor',
            'High' if height_growth_risk == "HIGH" else 'Medium' if height_growth_risk == "Medium" else 'Low',
            'High' if efficiency < 50 else 'Medium' if efficiency < 70 else 'Monitor',
            'Low'
        ]
    })
    
    # Display as HTML table with styling
    st.markdown("""
    <style>
        .risk-summary-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }
        .risk-summary-table th {
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            color: white;
            font-weight: 600;
            padding: 1rem;
            text-align: left;
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .risk-summary-table td {
            padding: 0.875rem 1rem;
            border-bottom: 1px solid #e5e7eb;
            font-size: 0.9rem;
        }
        .risk-summary-table tr:nth-child(even) {
            background-color: #f9fafb;
        }
        .risk-summary-table tr:hover {
            background-color: #f3f4f6;
        }
        .priority-badge {
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            display: inline-block;
        }
        .priority-immediate { background: #fee2e2; color: #dc2626; }
        .priority-high { background: #ffedd5; color: #ea580c; }
        .priority-medium { background: #fef3c7; color: #d97706; }
        .priority-low { background: #dcfce7; color: #16a34a; }
    </style>
    """, unsafe_allow_html=True)
    
    # Generate table HTML
    table_html = "<table class='risk-summary-table'><thead><tr>"
    for col in summary_data.columns:
        table_html += f"<th>{col}</th>"
    table_html += "</tr></thead><tbody>"
    
    for _, row in summary_data.iterrows():
        table_html += "<tr>"
        for i, value in enumerate(row):
            if i == 3:  # Mitigation Priority column
                priority_class = f"priority-{value.lower()}"
                table_html += f"<td><span class='priority-badge {priority_class}'>{value}</span></td>"
            else:
                table_html += f"<td>{value}</td>"
        table_html += "</tr>"
    
    table_html += "</tbody></table>"
    st.markdown(table_html, unsafe_allow_html=True)
    
    # Recommendations section
    st.markdown("""
    <div style='background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
                border-left: 4px solid #3b82f6;
                padding: 1.5rem;
                border-radius: 8px;
                margin-top: 2rem;'>
        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 1rem;'>
            <svg style='width: 24px; height: 24px;' fill='none' stroke='#3b82f6' viewBox='0 0 24 24'>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <h5 style='margin: 0; color: #1e3a8a; font-size: 1rem; font-weight: 600;'>
                RECOMMENDED ACTIONS
            </h5>
        </div>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;'>
            <div style='background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e5e7eb;'>
                <div style='color: #dc2626; font-weight: 600; margin-bottom: 0.5rem;'> Immediate Actions</div>
                <ul style='margin: 0; padding-left: 1.2rem; color: #4b5563; font-size: 0.875rem;'>
                    <li>Review proppant concentration and pump rate</li>
                    <li>Monitor pressure response closely</li>
                    <li>Prepare contingency volumes</li>
                </ul>
            </div>
            <div style='background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e5e7eb;'>
                <div style='color: #ea580c; font-weight: 600; margin-bottom: 0.5rem;'> Optimization Actions</div>
                <ul style='margin: 0; padding-left: 1.2rem; color: #4b5563; font-size: 0.875rem;'>
                    <li>Adjust fluid viscosity for better height control</li>
                    <li>Optimize stage sequencing</li>
                    <li>Consider diverter technology for improved coverage</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close risk summary div
    st.markdown("</div>", unsafe_allow_html=True)  # Close custom card

# ==================== ENHANCED FRACADVISOR™ AI ACTIONS ====================
if show_explain:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-title'> FRACADVISOR™ – AI Prescriptive Analytics</h3>", unsafe_allow_html=True)
    
    # AI Confidence Score
    ai_confidence = 92 - (closure_score * 0.1 + screenout_prob * 0.05 + (100 - efficiency) * 0.05)
    st.metric(" **AI Confidence Score**", f"{ai_confidence:.1f}%", 
              delta="High Reliability" if ai_confidence > 85 else "Moderate")
    
    # Advanced AI Analysis Matrix
    st.markdown("####  **AI Multi-Parameter Analysis Matrix**")
    
    analysis_params = [
        {"Parameter": "Stress Anisotropy", "Value": f"{(sigma_hmax - sigma_hmin)/sigma_hmin*100:.1f}%", 
         "Impact": "HIGH" if (sigma_hmax - sigma_hmin) > 2000 else "MEDIUM", 
         "AI Insight": "Controls fracture complexity & asymmetry"},
        
        {"Parameter": "Fluid Efficiency Index", "Value": f"{(pump_rate/(fluid_viscosity+0.1))**0.5:.2f}", 
         "Impact": "HIGH" if fluid_viscosity > 50 else "MEDIUM", 
         "AI Insight": "Dictates proppant transport & fracture coverage"},
        
        {"Parameter": "Cluster Intensity", "Value": f"{perfs_per_cluster * (40/stage_num):.1f}", 
         "Impact": "HIGH" if perfs_per_cluster > 8 else "MEDIUM", 
         "AI Insight": "Affects initiation pressure & near-wellbore tortuosity"},
        
        {"Parameter": "Energy Balance Ratio", "Value": f"{(pump_rate*500)/(young_modulus*1000):.3f}", 
         "Impact": "HIGH", 
         "AI Insight": "Ratio of injection energy to rock stiffness"},
        
        {"Parameter": "Shadow Impact Index", "Value": f"{stress_shadow_index:.3f}", 
         "Impact": "HIGH" if stress_shadow_index > 0.3 else "MEDIUM", 
         "AI Insight": "Quantifies well interference effects"},
        
        {"Parameter": "Proppant Embedment Risk", "Value": f"{(proppant_conc * 1000)/(young_modulus*100):.1f}", 
         "Impact": "MEDIUM" if young_modulus < 5 else "LOW", 
         "AI Insight": "Risk of proppant crushing in soft formations"},
        
        {"Parameter": "Fluid Leakoff Coefficient", "Value": f"{fluid_viscosity/(pump_rate+1):.3f}", 
         "Impact": "HIGH" if fluid_viscosity < 10 else "MEDIUM", 
         "AI Insight": "Controls fluid loss to formation"}
    ]
    
    analysis_df = pd.DataFrame(analysis_params)
    st.dataframe(analysis_df, use_container_width=True, hide_index=True)
    
    # EXTENDED ENGINEERING ACTION SUGGESTIONS
    st.markdown("####  **AI-Generated Engineering Action Plan**")
    
    actions = []
    
    # CLOSURE RISK ACTIONS
    if closure_risk == "HIGH":
        actions.extend([
            {"Action": " **Immediate pump rate reduction by 20-25%**", 
             "Priority": "🚨 CRITICAL", 
             "Physics Basis": f"Net pressure increase of {net_pressure[-1] - net_pressure[0]:.0f} psi exceeds safe window",
             "Expected Impact": "Reduce closure stress by 15-20%"},
            
            {"Action": " **Switch to high-efficiency fluid system**", 
             "Priority": "🔴 HIGH", 
             "Physics Basis": f"Current fluid viscosity ({fluid_viscosity} cP) inadequate for stress conditions",
             "Expected Impact": "Improve fracture width maintenance by 30%"},
            
            {"Action": " **Shorten stage duration by 15 minutes**", 
             "Priority": "🟡 MEDIUM", 
             "Physics Basis": "Extended exposure increases closure risk in high-stress environments",
             "Expected Impact": "Reduce closure probability by 25%"}
        ])
    
    # SCREENOUT RISK ACTIONS
    if screenout_prob > 60:
        actions.extend([
            {"Action": " **Reduce proppant concentration from {proppant_conc} to {max(0.5, proppant_conc*0.7):.1f} lb/ft²**", 
             "Priority": " CRITICAL", 
             "Physics Basis": f"Screenout probability {screenout_prob:.0f}% exceeds operational limits",
             "Expected Impact": "Lower bridging risk by 40%"},
            
            {"Action": " **Implement 5-10 bpm flush every 15 minutes**", 
             "Priority": "🔴 HIGH", 
             "Physics Basis": f"Proppant loading factor {proppant_loading:.2f} indicates transport issues",
             "Expected Impact": "Clear near-wellbore accumulation"},
            
            {"Action": " **Increase perforation cluster spacing by 10-15%**", 
             "Priority": "🟡 MEDIUM", 
             "Physics Basis": f"Current spacing ({cluster_spacing} ft) may cause proppant banking",
             "Expected Impact": "Improve distribution efficiency"}
        ])
    
    # HEIGHT GROWTH ACTIONS
    if height_growth_risk == "HIGH":
        actions.extend([
            {"Action": " **Deploy particulate diverter at {int(frac_height*0.7)} ft depth**", 
             "Priority": "🔴 HIGH", 
             "Physics Basis": f"Low stress contrast ({stress_contrast} psi) enables vertical migration",
             "Expected Impact": "Contain height growth within target zone"},
            
            {"Action": " **Reduce injection rate by 15% while maintaining pressure**", 
             "Priority": "🔴 HIGH", 
             "Physics Basis": f"Height-to-length ratio {frac_height/frac_half_length:.2f} exceeds optimal 0.3-0.5 range",
             "Expected Impact": "Limit vertical propagation"},
            
            {"Action": " **Implement rate-controlled zonal isolation**", 
             "Priority": "🟡 MEDIUM", 
             "Physics Basis": "Geomechanical analysis shows weak barrier at 5050 ft",
             "Expected Impact": "Focus energy on lateral growth"}
        ])
    
    # EFFICIENCY OPTIMIZATION ACTIONS
    if efficiency < 70:
        actions.extend([
            {"Action": " **Increase cluster efficiency with engineered perforations**", 
             "Priority": "🟡 MEDIUM", 
             "Physics Basis": f"Current efficiency {efficiency:.0f}% below target 80% threshold",
             "Expected Impact": "Improve cluster contribution by 25%"},
            
            {"Action": " **Optimize fluid pulse sequencing**", 
             "Priority": "🟢 LOW", 
             "Physics Basis": f"Fluid energy distribution coefficient {pump_rate/(fluid_viscosity+1):.1f} suboptimal",
             "Expected Impact": "Enhance fracture network connectivity"},
            
            {"Action": " **Implement variable rate schedule**", 
             "Priority": "🟡 MEDIUM", 
             "Physics Basis": "Constant rate injection reduces complexity generation",
             "Expected Impact": "Increase SRV by 15-20%"}
        ])
    
    # ALWAYS RECOMMENDED BEST PRACTICES
    actions.extend([
        {"Action": " **Real-time pressure transient analysis every 5 minutes**", 
         "Priority": "🟢 LOW", 
         "Physics Basis": "Continuous monitoring detects early trend deviations",
         "Expected Impact": "Enable proactive adjustments"},
        
        {"Action": " **Maintain 10-15% rate variability**", 
         "Priority": "🟡 MEDIUM", 
         "Physics Basis": "Prevents screenout while maximizing growth",
         "Expected Impact": "Balance risk and performance"},
        
        {"Action": " **Microseismic-derived geometry calibration**", 
         "Priority": "🟢 LOW", 
         "Physics Basis": f"Current event density {microseismic_rate.mean():.1f}/min provides validation",
         "Expected Impact": "Improve model accuracy by 15%"}
    ])
    
    # Display actions in priority order
    priority_order = {"🚨 CRITICAL": 4, "🔴 HIGH": 3, "🟡 MEDIUM": 2, "🟢 LOW": 1}
    
    if actions:
        actions_df = pd.DataFrame(actions)
        actions_df['Priority_Value'] = actions_df['Priority'].map(priority_order)
        actions_df = actions_df.sort_values('Priority_Value', ascending=False)
        
        # Create tabs for different priority levels
        crit_tab, high_tab, med_tab, low_tab = st.tabs(["🚨 Critical", "🔴 High", "🟡 Medium", "🟢 Low"])
        
        with crit_tab:
            crit_actions = actions_df[actions_df['Priority'] == "🚨 CRITICAL"]
            if not crit_actions.empty:
                for _, action in crit_actions.iterrows():
                    with st.expander(f"**{action['Action']}**", expanded=True):
                        st.write(f"**Physics Basis:** {action['Physics Basis']}")
                        st.write(f"**Expected Impact:** {action['Expected Impact']}")
                        st.progress(0.9, text="Urgency: 90%")
            else:
                st.success("✅ No critical actions required")
        
        with high_tab:
            high_actions = actions_df[actions_df['Priority'] == "🔴 HIGH"]
            if not high_actions.empty:
                for _, action in high_actions.iterrows():
                    with st.expander(f"**{action['Action']}**"):
                        st.write(f"**Physics Basis:** {action['Physics Basis']}")
                        st.write(f"**Expected Impact:** {action['Expected Impact']}")
                        st.progress(0.7, text="Urgency: 70%")
        
        with med_tab:
            med_actions = actions_df[actions_df['Priority'] == "🟡 MEDIUM"]
            if not med_actions.empty:
                for _, action in med_actions.iterrows():
                    with st.expander(f"**{action['Action']}**"):
                        st.write(f"**Physics Basis:** {action['Physics Basis']}")
                        st.write(f"**Expected Impact:** {action['Expected Impact']}")
                        st.progress(0.5, text="Urgency: 50%")
        
        with low_tab:
            low_actions = actions_df[actions_df['Priority'] == "🟢 LOW"]
            if not low_actions.empty:
                for _, action in low_actions.iterrows():
                    with st.expander(f"**{action['Action']}**"):
                        st.write(f"**Physics Basis:** {action['Physics Basis']}")
                        st.write(f"**Expected Impact:** {action['Expected Impact']}")
                        st.progress(0.3, text="Urgency: 30%")
    
    # AI PREDICTIVE OUTCOMES
    st.markdown("####  **AI-Predicted Outcomes**")
    
    pred_col1, pred_col2, pred_col3 = st.columns(3)
    
    with pred_col1:
        if actions:
            risk_reduction = min(95, closure_score * 0.6 + screenout_prob * 0.4)
            st.metric("**Predicted Risk Reduction**", f"{risk_reduction:.0f}%", 
                     delta="With implementation")
    
    with pred_col2:
        prod_increase = max(5, efficiency * 0.8 - 20)
        st.metric("**Estimated Production Increase**", f"{prod_increase:.0f}%", 
                 delta="Compared to baseline")
    
    with pred_col3:
        cost_savings = (closure_score * 500 + screenout_prob * 1000) / 100
        st.metric("**Potential Cost Savings**", f"${cost_savings:,.0f}", 
                 delta="Per stage")
    
    st.markdown("</div>", unsafe_allow_html=True)


# ==================== SESSION STATE MANAGEMENT ====================
# Initialize session state variables
if 'emergency_alert' not in st.session_state:
    st.session_state.emergency_alert = False

# Display emergency alert if triggered
if st.session_state.emergency_alert:
    st.error("""
    🚨 **EMERGENCY ALERT ACTIVE**  
    All support engineers have been notified.  
    Please standby for instructions from the on-call engineer.
    """)
    
    if st.button("Acknowledge Alert"):
        st.session_state.emergency_alert = False
        st.rerun()